from django import forms

class SearchForm(forms.Form):
    packages=forms.CharField(label="Paquetes", required=True, widget=forms.Textarea)