from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label="Your name",
        widget=forms.TextInput(attrs={"class": "contact-input"})
    )
    email = forms.EmailField(
        label="Your email",
        widget=forms.EmailInput(attrs={"class": "contact-input"})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 5, "class": "contact-input"})
    )