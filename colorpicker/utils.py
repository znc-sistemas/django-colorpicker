# coding: utf-8

# From https://github.com/timchurch/django-color-utils/blob/master/color_utils/utils.py
# From Stack Overflow: http://stackoverflow.com/a/214657


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return "rgb%s" % str(tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3)))


def rgb_to_tuple(rgb):
    return tuple(int(n) for n in rgb.replace('rgb(', '').replace(')', '').replace(' ', '').split(','))


def rgb_to_hex(rgb):
    if not type(rgb) == tuple:
        rgb = rgb_to_tuple(rgb)
    return '#%02x%02x%02x' % rgb


def alpha_hex_to_rgba(value):
    value = value.lstrip('#')
    lv = len(value)
    rgba = tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))
    rgba = rgba[1], rgba[2], rgba[3], rgba[0]
    return 'rgba%s' % str(rgba)


def rgba_to_tuple(rgba):
    return tuple(int(n) for n in rgba.replace('rgba(', '').replace(')', '').replace(' ', '').split(','))


def rgba_to_alpha_hex(rgba):
    if not type(rgba) == tuple:
        rgba = rgba_to_tuple(rgba)
    return '#%02x%02x%02x%02x' % (rgba[3], rgba[0], rgba[1], rgba[2])


def is_valid_rgb(rgb):
    r, g, b = rgb_to_tuple(rgb)
    if r < 0 or r > 255:
        return False
    if g < 0 or g > 255:
        return False
    if b < 0 or b > 255:
        return False
    return True


def is_valid_rgba(rgba):
    r, g, b, a = rgba_to_tuple(rgba)
    if r < 0 or r > 255:
        return False
    if g < 0 or g > 255:
        return False
    if b < 0 or b > 255:
        return False
    if a < 0 or a > 255:
        return False
    return True


def is_valid_hex(value):
    try:
        int(value[1:], 16)
    except:
        return False
    rgb = hex_to_rgb(value)
    return is_valid_rgb(rgb)


def is_valid_alpha_hex(value):
    try:
        int(value[1:], 16)
    except:
        return False
    rgba = alpha_hex_to_rgba(value)
    return is_valid_rgba(rgba)
