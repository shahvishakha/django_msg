from django import forms
from dj_msg.models import Contact

class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=255)
    # last_name = forms.CharField(max_length=255)
    # email_address = forms.EmailField(max_length=250)
    # message = forms.CharField(widget=forms.Textarea, max_length=255)

    class Meta:
        model = Contact
        fields = ("first_name","last_name","email_address","message")