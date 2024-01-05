from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
import sqlite3


sections = [
    {'title': 'Главная страница', 'url_name': 'main'},
    {'title': 'Меню', 'url_name': 'menu'}
]

goods = [
    {'id': 0, 'name': 'Пепперони', 'price': 300, 'img': 'peperoni.png', 'descr': 'dwewe'},
    {'id': 1, 'name': 'Четыре сыра', 'price': 250, 'img': 'cheese.png', 'descr': 'dwewe'},
    {'id': 2, 'name': 'Гавайская', 'price': 350, 'img': 'hawaii.png', 'descr': 'dwewe'},
    {'id': 3, 'name': 'Маргарита', 'price': 200, 'img': 'margarita.png', 'descr': 'dwewe'},
    {'id': 4, 'name': 'Четыре сезона', 'price': 450, 'img': 'cheese.png', 'descr': 'dwewe'},
    {'id': 5, 'name': 'Ветчина с грибами', 'price': 330, 'img': 'grib.png', 'descr': 'dwewe'},
    {'id': 6, 'name': 'Песто', 'price': 400, 'img': 'bekon.png', 'descr': 'dwewe'},
]


def main(request: HttpRequest):
    a = []
    data = {
        'title': 'Меню',
        'sections': sections
    }
    return render(request, 'menu/main.html', context=data)


def menu(request: HttpRequest):
    con = {
        'title': 'Меню',
        'sections': sections,
        'menu': goods
    }
    return render(request, 'menu/menu.html', context=con)


def pizza(request: HttpRequest, pizza_id: int):
    return HttpResponse('Пицца')


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')
