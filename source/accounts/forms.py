from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, EmailField, CharField


class MyUserCreationForm(UserCreationForm):
    email = EmailField(required=True, max_length=150)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        # widgets = {
        #     'email': EmailField(required=True, max_length=None)
        # }

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if not first_name and not last_name:
            raise forms.ValidationError(
                "You should fill one of the fields First name or Last name",
                code='Incorrect First_name or Last_name'
            )
