from django import forms
import re


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
