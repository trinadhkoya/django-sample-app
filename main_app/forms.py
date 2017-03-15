from django import forms

# class TreasureForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     value = forms.DecimalField(max_digits=10, decimal_places=2)
#     material = forms.CharField(max_length=100)
#     location = forms.CharField(max_length=100)
#     img_url = forms.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
from .models import Treasure

'''
the above method is little lengthy,if we have another simple strategy that is nothing but meta
'''


class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'location', 'img_url', 'material', 'user']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, label='User Name')
    password = forms.CharField(widget=forms.PasswordInput())
