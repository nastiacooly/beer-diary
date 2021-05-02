from django.shortcuts import render
from django.views import generic

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


# Создаем класс для отображения всех обзоров пива
class BeerReviewListView(generic.ListView):
    model = BeerReview
    queryset = BeerReview.objects.all().order_by('name')