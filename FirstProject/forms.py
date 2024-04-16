from django import forms
from FirstProject.models import Housing
from django.core.exceptions import ValidationError


class HousingForm(forms.Form):
    area = forms.IntegerField(min_value=10, max_value=1900, help_text="Введите площадь жилья (м²)")
    address = forms.CharField(max_length=100, help_text="Укажите адрес жилья")
    cost = forms.IntegerField(min_value=10, max_value=100000000000, help_text="Введите стоимость жилья")

'''
    def valid_area(self):
        area = self.cleaned_data['area']

        if area > 1000:
            raise ValidationError("Вы точно вводите верную площадь?")
        return area
'''