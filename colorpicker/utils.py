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


# RRGGBBAA
def alpha_hex_to_rgba(value):
    value = value.lstrip('#')
    lv = len(value)
    rgba = tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))
    return 'rgba%s' % str(rgba)


def rgba_to_tuple(rgba):
    rgba_list = []
    for n in rgba.replace('rgba(', '').replace(')', '').replace(' ', '').split(','):
        if '.' in n:
            rgba_list.append(float(n))
        else:
            rgba_list.append(int(n))
    return tuple(rgba_list)


# RRGGBBAA
def rgba_to_alpha_hex(rgba):
    if not type(rgba) == tuple:
        rgba = rgba_to_tuple(rgba)
    return '#%02x%02x%02x%02x' % rgba


def is_valid_rgb(rgb):
    try:
        r, g, b = rgb_to_tuple(rgb)
    except:
        return False
    if r < 0 or r > 255:
        return False
    if g < 0 or g > 255:
        return False
    if b < 0 or b > 255:
        return False
    return True


def is_valid_rgba(rgba):
    try:
        r, g, b, a = rgba_to_tuple(rgba)
    except:
        return False
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


# RRGGBBAA
def is_valid_alpha_hex(value):
    try:
        int(value[1:], 16)
    except:
        return False
    rgba = alpha_hex_to_rgba(value)
    return is_valid_rgba(rgba)
