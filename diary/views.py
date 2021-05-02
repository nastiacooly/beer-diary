from django.shortcuts import render
from .models import BeerReview, BeerType

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """    
    # Обзоры с наивысшим рейтингом
    perfect_beers = BeerReview.objects.filter(rating__exact='5')

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'perfect_beers':perfect_beers},
    )
