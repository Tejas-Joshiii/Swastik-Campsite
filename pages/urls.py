from django.urls import path

from . import views


app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("stay-options/", views.stay_options, name="stay_options"),
    path("experiences/", views.experiences, name="experiences"),
    path("location/", views.location, name="location"),
    path("contact/", views.contact, name="contact"),
]
