from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.about_view, name='about'),

    path('skills/', views.skills_view, name='skills'),
    path('experience/', views.experience_view, name='experience'),
    path('projects/', views.projects_view, name='projects'),

    path('education/', views.education_view, name='education'),
    path('certificates/', views.certificates_view, name='certificates'),
    path('languages/', views.languages_view, name='languages'),
    path("contact/", views.contact_view, name="contact"),

    path("animes/", views.favorite_animes, name="animes"),
    path("movies/", views.favorite_movies, name="movies"),
    path("bands/", views.favorite_bands, name="bands"),
    path("test-email/", views.test_email),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)