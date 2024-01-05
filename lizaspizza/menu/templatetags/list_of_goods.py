from django import template
from menu.views import goods
from django.templatetags.static import static


register = template.Library()


@register.simple_tag()
def list_of_goods(row_len: int = 3):
    menu = []
    row = []
    c = 1
    for g in goods:
        row.append(g)
        if c == row_len:
            menu.append(row)
            row = []
            c = 0
        c += 1
    return menu


@register.simple_tag()
def good_img(img_url: str):
    return static("menu/images/" + img_url)
