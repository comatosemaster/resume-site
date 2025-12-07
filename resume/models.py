from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(blank=True)  # <- FULL ABOUT PAGE CONTENT

    hero_heading = models.CharField(max_length=200, blank=True)
    hero_subheading = models.CharField(max_length=300, blank=True)
    hero_description = models.TextField(blank=True)
    hero_button_primary = models.CharField(max_length=100, blank=True)
    hero_button_primary_link = models.URLField(blank=True)
    hero_button_secondary = models.CharField(max_length=100, blank=True)
    hero_button_secondary_link = models.URLField(blank=True)

    hero_typing_text = models.TextField(blank=True)
    hero_highlight_1 = models.CharField(max_length=200, blank=True)
    hero_highlight_2 = models.CharField(max_length=200, blank=True)
    hero_highlight_3 = models.CharField(max_length=200, blank=True)

    stat_title_1 = models.CharField(max_length=120, blank=True)
    stat_value_1 = models.CharField(max_length=50, blank=True)

    stat_title_2 = models.CharField(max_length=120, blank=True)
    stat_value_2 = models.CharField(max_length=50, blank=True)

    stat_title_3 = models.CharField(max_length=120, blank=True)
    stat_value_3 = models.CharField(max_length=50, blank=True)

    stat_title_4 = models.CharField(max_length=120, blank=True)
    stat_value_4 = models.CharField(max_length=50, blank=True)

    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("hard", "Hard Skill"),
        ("soft", "Soft Skill"),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} – {self.company}"


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    github = models.URLField(blank=True)
    demo = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} – {self.institution}"


class Certificate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


LANGUAGE_LEVELS = [
    ("BASIC", "Basic"),
    ("INTERMEDIATE", "Intermediate"),
    ("ADVANCED", "Advanced"),
    ("FLUENT", "Fluent"),
    ("NATIVE", "Native"),
]

class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LANGUAGE_LEVELS)

    def __str__(self):
        return f"{self.name} – {self.level}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.email} ({self.created_at:%Y-%m-%d})"
