from django.contrib import admin
from .models import Profile, Skill, Experience, Project
from .models import Education, Certificate, Language
from .models import ContactMessage


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "profile")
    list_filter = ("category",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date")
    list_filter = ("company",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "profile")


admin.site.register(Profile)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Language)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    ordering = ("-created_at",)