from django.shortcuts import render
from django.views import generic

from .models import BeerReview, BeerType

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """    
    # Обзоры с наивысшим рейтингом
    perfect_beers = BeerReview.objects.filter(rating__exact='5')

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'perfect_beers':perfect_beers, 'num_visits':num_visits},
    )

# Создаем класс для отображения всех обзоров пива
class BeerReviewListView(generic.ListView):
    model = BeerReview
    queryset = BeerReview.objects.all().order_by('name')
    paginate_by = 15

# Класс для отображения каждого отдельного обзора
class BeerReviewDetailView(generic.DetailView):
    model = BeerReview