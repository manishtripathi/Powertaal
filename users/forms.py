from django import forms
from .models.models import FreeUser
from .models.adminlogin import AdminLogin

class RegistrationForm(forms.ModelForm):
    confirmEmail = forms.EmailField();
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FreeUser
        fields = ['UserName', 'Place']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("UserName")
        confirm_email = cleaned_data.get("confirmEmail")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmPassword")
        if email != confirm_email:
            raise forms.ValidationError("Emails do not match")
        if password !=confirm_password: 
            raise forms.ValidationError("Password do not match")
        
        return cleaned_data
            
class AdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }