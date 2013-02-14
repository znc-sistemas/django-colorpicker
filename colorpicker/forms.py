#coding: utf-8
from django import forms
# from utils import (is_valid_alpha_hex, is_valid_hex, is_valid_rgb,
#     is_valid_rgba, rgba_to_alpha_hex, rgb_to_hex, hex_to_rgb)


class ColorField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(ColorField, self).__init__(*args, **kwargs)
