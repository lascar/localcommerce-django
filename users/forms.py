# users/forms.py
import pdb
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    password = auth_forms.ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"password/\">this form</a>."))
    # pdb.set_trace()
    # obtains: http://es.localhost:8000/gestion/users/customuser/1/change/password/
    # want: http://es.localhost:8000/gestion/users/customuser/1/password/

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'dirrection1',\
                  'dirrection2', 'town', 'zipcode', 'state', 'country',\
                  'telephone1', 'telephone2', 'is_staff', 'is_active') 
        # fields = ('__all__')


    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]
