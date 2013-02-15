# -*- coding: utf-8 -*-

from django.core.validators import ValidationError
from django.db.models import CharField
from widgets import ColorPickerWidget
from forms import ColorField as ColorFormField
from utils import (is_valid_alpha_hex, is_valid_hex, is_valid_rgb,
    is_valid_rgba, rgba_to_alpha_hex, rgb_to_hex, hex_to_rgb)

FORMAT_RGB = 'rgb'
FORMAT_HEX = 'hex'
FORMAT_RGBA = 'rgba'
FORMAT_HEXA = 'hexa'

FORMATS = (FORMAT_RGB, FORMAT_HEX, FORMAT_RGB, FORMAT_HEXA)


class ColorField(CharField):

    def __init__(self, format='hex', *args, **kwargs):
        kwargs['max_length'] = 25
        self.format = format
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, *args, **kwargs):
        kwargs['widget'] = ColorPickerWidget(format=self.format)
        kwargs['form_class'] = ColorFormField
        return super(ColorField, self).formfield(*args, **kwargs)

    def clean(self, value, model_instance):
        '''
            Valida cores nos formatos RGB RGBA #RRGGBB e #RRGGBBAA
        '''
        import re
        invalid = 'Cor %s inválida' % self.format.upper()
        value = value.replace(' ', '')

        if self.format == FORMAT_RGB:
            regex = re.compile("rgb\(\d{1,3},\d{1,3},\d{1,3}\)",
                re.IGNORECASE | re.UNICODE)
            is_valid = is_valid_rgb
        elif self.format == FORMAT_RGBA:
            regex = re.compile("rgba\((?P<r>\d{1,3}),(?P<g>\d{1,3}),(?P<b>\d{1,3}),(?P<a>(0\.\d+)|\d)\)",
                re.IGNORECASE | re.UNICODE)
            is_valid = is_valid_rgba
        elif format == FORMAT_HEXA:
            regex = re.compile("#([A-Fa-f\d]{8}|[A-Fa-f\d]{6}|[A-Fa-f\d]{3})",
                re.IGNORECASE | re.UNICODE)
            is_valid = is_valid_alpha_hex
        else:
            regex = re.compile("#([A-Fa-f\d]{8}|[A-Fa-f\d]{6}|[A-Fa-f\d]{3})",
                re.IGNORECASE | re.UNICODE)
            is_valid = is_valid_hex

        if len(regex.findall(value)) != 1:
            raise ValidationError(invalid)
        if not is_valid(value):
            raise ValidationError(invalid)

        return super(ColorField, self).clean(value, model_instance)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^colorpicker\.models\.ColorField"])
except ImportError:
    pass
