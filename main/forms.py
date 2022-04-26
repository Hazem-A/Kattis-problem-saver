from django import forms

#This creates the parameters of the form which django will automatically generate the html for us
class Createlist(forms.Form):
    name = forms.CharField(max_length=300)

