from django import forms

from fast_foods.models import Fastfood


class FastfoodForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FastfoodForm, self).__init__(*args, **kwargs)
        self.fields['city'].required = False
        self.fields['name'].required = True
        self.fields['address'].required = True

    class Meta:
        model = Fastfood
        fields = '__all__'