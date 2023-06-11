from django import forms

class FeedbackForm(forms.Form):
    email = forms.CharField(max_length=50, label='Your Mail:')
    feedback = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':5}))