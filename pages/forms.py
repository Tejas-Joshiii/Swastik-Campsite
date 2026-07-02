from django import forms

from .models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "email@example.com"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us about your travel plans...", "rows": 5}),
        }
