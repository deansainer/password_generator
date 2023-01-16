from django import forms


class IndexForm(forms.Form):
    password_length = forms.IntegerField(required=True)


