# -*- encoding: utf-8 -*-
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe


class ColorPickerWidget(TextInput):

    def __init__(self, format='rgb', as_component=False, attrs=None):
        self.format = format
        self.as_component = as_component
        attrs_default = {'class': 'colorpicker'}
        if attrs:
            attrs_default.update(attrs)
        attrs_default.update({'data-color-format': self.format})

        if self.as_component:
            super(ColorPickerWidget, self).__init__(attrs=attrs)
        else:
            super(ColorPickerWidget, self).__init__(attrs=attrs_default)

    class Media:
        js = (
            'colorpicker/bootstrap-colorpicker.js',
            'colorpicker/init_colorpicker.js',
        )

        css = {'all': ('colorpicker/colorpicker.css',)}

    def render(self, name, value, attrs=None):
        result = super(ColorPickerWidget, self).render(name, value, attrs)

        css_bg = value
        if not value:
            if self.format == 'rgba':
                css_bg = 'rgba(255,255,255,0)'
            else:
                css_bg = 'rgb(255,255,255)'

        if self.as_component:
            result = u'''
            <div class="colorpicker input-append color" data-color="%s" data-color-format="%s">
                %s<span class="add-on">
                    <i style="background-color: %s"></i>
                </span>
            </div>''' % (css_bg,
                         self.format,
                         result,
                         css_bg)

        return mark_safe(result)
