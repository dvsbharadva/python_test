from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns  = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="About Us"),
    path("web/", views.web, name="Web Development"),
    path("cyber/", views.cyber, name="Cyber Securities"),
    path("contact/", views.contact, name="Contact Us"),
    path("domain/", views.domain, name="Domain & Hosting"),
]
