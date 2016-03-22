from django import forms

class chooseBattle(forms.Form):
    group = forms.CharField(label='Your name', max_length=100)