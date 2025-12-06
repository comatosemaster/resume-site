from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),

    path('skills/', views.skills_view, name='skills'),
    path('experience/', views.experience_view, name='experience'),
    path('projects/', views.projects_view, name='projects'),

    path('education/', views.education_view, name='education'),
    path('certificates/', views.certificates_view, name='certificates'),
    path('languages/', views.languages_view, name='languages'),
    path("contact/", views.contact_view, name="contact"),
]
