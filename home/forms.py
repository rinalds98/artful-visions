from django import forms
from .models import Contact, Faq


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class FaqSubmissionForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question']
