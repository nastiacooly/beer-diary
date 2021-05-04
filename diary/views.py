from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import BeerReview, BeerType

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_visits':num_visits},
    )

# Создаем класс для отображения всех обзоров пива
class BeerReviewListView(LoginRequiredMixin, generic.ListView):
    model = BeerReview
    paginate_by = 15
    def get_queryset(self):
        return BeerReview.objects.filter(creator=self.request.user).order_by('name')

# Класс для отображения каждого отдельного обзора
class BeerReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = BeerReview
    def get_queryset(self):
        return BeerReview.objects.filter(creator=self.request.user)

# Класс для отображения обзоров залогиненного пользователя с наивысшим рейтингом
class PefectBeerReviewsByUserListView(LoginRequiredMixin, generic.ListView):
    model = BeerReview
    context_object_name = 'beer_reviews_perfect_list'
    template_name ='diary/beerreview_list_created_user.html'
    paginate_by = 5
    def get_queryset(self):
        return BeerReview.objects.filter(creator=self.request.user).filter(rating__exact='5').order_by('name')