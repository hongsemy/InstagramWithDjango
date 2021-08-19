from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import User

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class SignUpForm(forms.ModelForm):
    # TODO: Implement html and css for signup and login page.
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']

        # PasswordInput: Enables an option for hidden password input.
        # placeholder: Following string will hold the place before any input is given.
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
