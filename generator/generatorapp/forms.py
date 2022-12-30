from django import forms


class IndexForm(forms.Form):
    password_length = forms.IntegerField(required=True)

    CHOICES = [
        ('Only letters', 'Only letters'),
        ('Letters & Numbers', 'Letters & Numbers'),
        ('Letters & Numbers & Special numbers', 'Letters & Numbers & Special numbers'),
    ]
    radio_buttons = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

