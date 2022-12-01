import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings


def validator(value):
    start_date = datetime.datetime.fromisoformat("2000-01-01")
    if not start_date.date() <= value <= datetime.datetime.now().date():
        raise ValidationError(["Неверные данные"], code='invalid')


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(format='%YYYY-%MM-%DD', attrs={'type': 'date'}), validators=[validator], label="Укажите дату:", error_messages={'invalid': 'Неверные данные'})

