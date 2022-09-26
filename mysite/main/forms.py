from django import forms

class CreateEvent(forms.Form):
    name = forms.CharField(label="name", min_length=2, max_length=200, required=True)
    date = forms.DateField(label="date", required=True)