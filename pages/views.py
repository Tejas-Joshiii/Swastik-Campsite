from django.contrib import messages
from django.db import DatabaseError, OperationalError
from django.shortcuts import redirect, render

from .forms import ContactInquiryForm


def home(request):
    return render(request, "pages/home.html")


def stay_options(request):
    return render(request, "pages/stay_options.html")


def experiences(request):
    return render(request, "pages/experiences.html")


def location(request):
    return render(request, "pages/location.html")


def contact(request):
    if request.method == "POST":
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except (DatabaseError, OperationalError):
                # Demo deployments may not have a writable database configured.
                pass
            messages.success(request, "Thanks, your message has been received. We will get back to you soon.")
            return redirect("pages:contact")
    else:
        form = ContactInquiryForm()

    return render(request, "pages/contact.html", {"form": form})
