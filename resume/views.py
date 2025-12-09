from django.shortcuts import render
from .models import Profile
from .models import Education, Certificate, Language, Profile
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ContactForm
from .models import ContactMessage, Profile
from .models import FavoriteItem


def get_profile():
    return Profile.objects.first()  # your single profile


def about_view(request):
    profile = get_profile()
    return render(request, "resume/about.html", {"profile": profile})

def skills_view(request):
    profile = get_profile()

    # Fetch all hard skills
    hard_skills = profile.skills.filter(category="hard").order_by("name")

    # Group them by skill_group
    grouped_hard = {}
    for skill in hard_skills:
        group = skill.skill_group or "Other"
        grouped_hard.setdefault(group, []).append(skill)

    # CUSTOM ORDER for groups
    GROUP_ORDER = [
        "Programming & Scripting",
        "Systems & Platforms",
        "Testing Methodologies",
        "Testing Tools",
        "Additional",
        "Other",
    ]

    # Sort groups by GROUP_ORDER
    grouped_hard = dict(
        sorted(
            grouped_hard.items(),
            key=lambda x: GROUP_ORDER.index(x[0]) if x[0] in GROUP_ORDER else 999
        )
    )

    # Soft skills — no grouping, alphabetical
    skills_soft = profile.skills.filter(category="soft").order_by("name")

    return render(request, "resume/skills.html", {
        "profile": profile,
        "grouped_hard": grouped_hard,
        "skills_soft": skills_soft,
    })


def experience_view(request):
    profile = get_profile()
    return render(request, "resume/experience.html", {
        "profile": profile,
        "experiences": profile.experiences.all()
    })


def projects_view(request):
    profile = get_profile()
    return render(request, "resume/projects.html", {
        "profile": profile,
        "projects": profile.projects.all()
    })


def education_view(request):
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('-start_year')
    return render(request, "resume/education.html", {
        "profile": profile,
        "education": education,
    })


def certificates_view(request):
    profile = Profile.objects.first()
    certificates = Certificate.objects.filter(profile=profile)

    return render(request, "resume/certificates.html", {
        "profile": profile,
        "certificates": certificates,
    })


def languages_view(request):
    profile = Profile.objects.first()
    languages = Language.objects.all().order_by('-level')
    return render(request, "resume/languages.html", {
        "profile": profile,
        "languages": languages,
    })


def contact_view(request):
    profile = Profile.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message_text = form.cleaned_data["message"]

            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_text,
            )

            subject = f"New message from {name} via portfolio"
            full_message = (
                f"From: {name} <{email}>\n\n"
                f"Message:\n{message_text}"
            )

            send_mail(
                subject,
                full_message,
                None,
                ["heyitsdavit@gmail.com"],
            )

            messages.success(request, "Thanks, your message has been sent.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "resume/contact.html", {
        "profile": profile,
        "form": form,
    })

from django.shortcuts import render
from .models import FavoriteItem


def favorite_animes(request):
    profile = get_profile()
    animes = FavoriteItem.objects.filter(category__iexact="anime")
    return render(request, "resume/animes.html", {
        "profile": profile,
        "animes": animes,
    })


def favorite_movies(request):
    profile = get_profile()
    movies = FavoriteItem.objects.filter(category__iexact="movie")
    return render(request, "resume/movies.html", {
        "profile": profile,
        "movies": movies,
    })


def favorite_bands(request):
    profile = get_profile()
    bands = FavoriteItem.objects.filter(category__iexact="band")
    return render(request, "resume/bands.html", {
        "profile": profile,
        "bands": bands,
    })
