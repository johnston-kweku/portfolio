from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username', 'email'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists.")
        return email
        