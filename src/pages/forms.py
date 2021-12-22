from django import forms

class UsernameForm(forms.Form):
    placeholder = "Your last.fm username (e.g. amirashabani)"
    attributes = {
        "placeholder": placeholder,
        "id": "username",
    }

    username = forms.CharField(
        required=False,
        label="",
        max_length=50,
        widget=forms.TextInput(attrs=attributes),
    )


