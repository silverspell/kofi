from django import forms


class TestForm(forms.Form):
    user = forms.CharField(max_length = 100)
    passw = forms.CharField(max_length = 50)


class PostdataForm(forms.Form):
    data = forms.CharField(label="Data", max_length=100)
