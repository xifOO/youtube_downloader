from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label="Youtube video url", max_length=255, widget=forms.TextInput(attrs={
        "class": "form-control",
    }))

