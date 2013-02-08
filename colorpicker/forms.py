#coding: utf-8
from django import forms
from django.core.validators import EMPTY_VALUES
from utils import (is_valid_alpha_hex, is_valid_hex, is_valid_rgb,
    is_valid_rgba, rgba_to_alpha_hex, rgb_to_hex)


class ColorField(forms.CharField):
    def to_python(self, value):
        if value in EMPTY_VALUES:
            return None
        return value

    def clean(self, value):
        super(ColorField, self).clean(value)
        if not self.required:
            if value == None or value == '':
                return None
        import re

        value = value.replace(' ', '')

        if value.startswith('#'):
            regex = re.compile("#([A-Fa-f\d]{8}|[A-Fa-f\d]{6}|[A-Fa-f\d]{3})",
                re.IGNORECASE | re.UNICODE)
            if len(value) == 9:
                is_valid = is_valid_alpha_hex
            else:
                is_valid = is_valid_hex
            convert = lambda x: x

        elif value.startswith('rgba'):
            regex = re.compile("rgba\(\d{1,3},\d{1,3},\d{1,3},\d{1,3}\)",
                re.IGNORECASE | re.UNICODE)
            is_valid = is_valid_rgba
            convert = rgba_to_alpha_hex
        else:
            regex = re.compile("rgb\(\d{1,3},\d{1,3},\d{1,3}\)",
                re.IGNORECASE | re.UNICODE)
            is_valid = is_valid_rgb
            convert = rgb_to_hex

        if len(regex.findall(value)) != 1:
            raise forms.ValidationError('Cor RGB inválida')
        if not is_valid(value):
            raise forms.ValidationError('Cor RGB inválida')

        return convert(value)
