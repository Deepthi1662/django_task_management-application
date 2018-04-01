from django.utils.translation import ugettext_lazy as _
from django import forms
from users.models import TaskUser


class TaskUserForm(forms.ModelForm):
    """
    User Registration form (Model Form)
    """
    error_messages = {
        'emails_exists': 'Email Already Registered Please enter valid Email',
        'number_exists': 'Number Already Registered Please enter valid Number',
        'username_exists': 'Username Already Registered Please enter valid Username',
        'password_mismatch': 'Password and Confirm Password Mismatched'
    }

    class Meta:
        model = TaskUser
        fields = ('first_name', 'last_name', 'email', 'number',
                  'username', 'password1', 'password2')

    first_name = forms.CharField(
        max_length=50, required=True,
        label=_('Enter First Name'))

    last_name = forms.CharField(
        max_length=50, required=True,
        label=_('Enter Last Name'))

    email = forms.EmailField(
        max_length=100, required=True,
        label=_('Enter Valid Email'))

    number = forms.IntegerField(
        label=_('Enter Valid Number'))

    username = forms.CharField(
        max_length=100, required=True,
        label=_('Enter User Name'))

    password1 = forms.CharField(
        max_length=30, required=True,
        widget=forms.PasswordInput,
        label=_('Enter Password'))

    password2 = forms.CharField(
        max_length=30, required=True,
        widget=forms.PasswordInput,
        label=_(' Enter Confirm Password'))

    def __init__(self, *args, **kwargs):
        super(TaskUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['number'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean_number(self):
        """
        Validating user contact number
        :return:
        """
        number = self.cleaned_data.get('number')
        if number in [user.number for user in TaskUser.objects.all()]:
            raise forms.ValidationError(
                self.error_messages['number_exists']
            )
        return number

    def clean_email(self):
        """
        Validating User Contact Email
        :return:
        """
        email = self.cleaned_data.get('email')
        if email in [user.email for user in TaskUser.objects.all()]:
            raise forms.ValidationError(
                self.error_messages['emails_exists']
            )
        return email

    def clean_password2(self):
        """
        Validating User Password
        :return:
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch']
            )
        return password2

    def save(self, commit=True):
        user = super(TaskUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user