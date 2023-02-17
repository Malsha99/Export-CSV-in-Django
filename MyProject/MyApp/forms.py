from django import forms

Format_Choices = (
    ('CSV','CSV'),
)

class FormatForm(forms.Form):
    format = forms.ChoiceField(choices=Format_Choices,widget=forms.Select(attrs={'class':'form-select'}))
    
