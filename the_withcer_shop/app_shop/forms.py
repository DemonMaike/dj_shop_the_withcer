from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FeedbackForm(forms.Form):
    email = forms.CharField(max_length=50, label='Your Mail:')
    feedback = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':5}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')