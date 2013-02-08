# -*- coding: utf-8 -*-

from django.db.models import CharField
from widgets import ColorPickerWidget
from forms import ColorField as ColorFormField


class ColorField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(ColorField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "ColorField"

    def formfield(self, *args, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        kwargs['form_class'] = ColorFormField
        return super(ColorField, self).formfield(*args, **kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^colorpicker\.models\.ColorField"])
except ImportError:
    pass
