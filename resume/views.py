from django.shortcuts import render
from .models import Profile
from .models import Education, Certificate, Language, Profile
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ContactForm
from .models import ContactMessage, Profile


def get_profile():
    return Profile.objects.first()  # your single profile


def about_view(request):
    profile = get_profile()
    return render(request, "resume/about.html", {"profile": profile})


def skills_view(request):
    profile = get_profile()
    skills_hard = profile.skills.filter(category="hard")
    skills_soft = profile.skills.filter(category="soft")
    return render(request, "resume/skills.html", {
        "profile": profile,
        "skills_hard": skills_hard,
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

            # Save to DB
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_text,
            )

            # Send email to you
            subject = f"New message from {name} via portfolio"
            full_message = (
                f"From: {name} <{email}>\n\n"
                f"Message:\n{message_text}"
            )

            send_mail(
                subject,
                full_message,
                None,  # uses DEFAULT_FROM_EMAIL
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