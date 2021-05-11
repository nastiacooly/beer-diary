from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BeerReview, BeerType
from .forms import UpdateBeerReviewForm, AddNewBeerReviewForm, NewUserForm, SearchBeerForm, FilterReviewsForm

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

def register_request(request):
    """
    Функция отображения регистрационной формы
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Registration succesful. You are now logged in as {request.user}.")
            return redirect('index')
        messages.error(
            request, 
            "Unsuccessful registration. Invalid information. Please read the requirements carefully and be sure to complete all the required(*) fields."
            )
    
    form = NewUserForm()
    return render(
        request,
        'register.html',
        context={"register_form": form}
    )

# Создаем класс для отображения всех обзоров пива в виде списка
class BeerReviewListView(LoginRequiredMixin, generic.ListView):
    model = BeerReview
    paginate_by = 15
    def get_queryset(self):
        return BeerReview.objects.filter(creator=self.request.user).order_by('name')

# Класс для отображения каждого отдельного обзора на отдельной странице
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


@login_required
def add_new_beer_review(request):
    """
    Функция отображения формы для добавления нового обзора
    """
    if request.method == "POST":
        form = AddNewBeerReviewForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            # и добавление записи в базу данных
            new_beer_review = BeerReview(
                creator=request.user, 
                image=form.cleaned_data['beer_image'], 
                name=form.cleaned_data['beer_name'],
                beertype=form.cleaned_data['beer_type'],
                rating=form.cleaned_data['beer_rating'],
                comments=form.cleaned_data['comments']
            )
            
            new_beer_review.save()

            # Переход по адресу 'beers' (see all):
            return HttpResponseRedirect(reverse('beers') )
        messages.error(
            request, 
            "Your beer review contains invalid data. Please try again."
            )

    # Если GET, создать форму по умолчанию.
    else:
        form = AddNewBeerReviewForm()

    return render(
        request, 
        'diary/add_new_beer_review.html', 
        context={'form': form},
    )


@login_required
def update_beer_review(request, pk):
    """
    Функция отображения формы для изменения/обновления обзора
    """
    # Get beer review object only if the requester is the creator of the review or 404
    beer_review = get_object_or_404(BeerReview.objects.filter(creator=request.user), pk=pk)

    if request.method == "POST":
        form = UpdateBeerReviewForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            # и сохранение базы данных
            beer_review.image = form.cleaned_data['beer_image']
            beer_review.name = form.cleaned_data['beer_name']
            beer_review.beertype = form.cleaned_data['beer_type']
            beer_review.rating = form.cleaned_data['beer_rating']
            beer_review.comments = form.cleaned_data['comments']
            
            beer_review.save()

            # Переход по адресу 'beers' (see all):
            return HttpResponseRedirect(reverse('beers') )
        messages.error(
            request, 
            "Your beer review contains invalid data. Please try again."
            )

    # Если это GET, создать форму по умолчанию.
    else:
        form = UpdateBeerReviewForm(initial={
            'beer_image': beer_review.image, 
            'beer_name': beer_review.name, 
            'beer_type': beer_review.beertype, 
            'beer_rating': beer_review.rating, 
            'comments': beer_review.comments
            })

    return render(
        request, 
        'diary/update_beer_review.html', 
        context={'form': form, 'beer_review': beer_review},
    )

@login_required
def delete_beer_review(request, pk):
    """
    Функция отображения для удаления обзора
    """
    # Get beer review object only if the requester is the creator of the review or 404
    beer_review = get_object_or_404(BeerReview.objects.filter(creator=request.user), pk=pk)

    if request.method == "POST":
        beer_review.delete()

        # Переход по адресу 'beers' (see all):
        return HttpResponseRedirect(reverse('beers') )
    
    return render(
        request,
        'diary/delete_beer_review.html',
        context={'beer_review': beer_review},
    )

@login_required
def beer_search(request):
    """
    Функция отображения для поиска обзора
    """
    reviews = []
    form = SearchBeerForm()
    query = request.GET.get('beer_name')
    if query:
        reviews = BeerReview.objects.filter(creator=request.user
            ).filter(name__icontains=query
            ).order_by('name')
        if reviews:
            messages.success(request, "Found")
        else:
            messages.error(
            request,
            "Not found in your diary"
        )

    return render(
        request,
        'diary/search.html',
        context={"form": form, 'reviews': reviews},
    )

@login_required
def beers_filter(request):
    """
    Функция отображения для фильтрации обзоров (по типу и рейтингу)
    """

    reviews = []

    def check_result():
        """
        For success/error messages depending on filter results
        """
        if reviews:
            messages.success(request, "Found filter match")
        else:
            messages.error(
            request,
            "No filter match"
        )
    
    form = FilterReviewsForm(initial={'beer_rating': '---'})
    query_type = request.GET.get('beer_type')
    query_rating = request.GET.get('beer_rating')

    if query_type and query_rating:
        reviews = BeerReview.objects.filter(creator=request.user
            ).filter(beertype__exact=query_type
            ).filter(rating__exact=query_rating
            ).order_by('name')
        check_result()
    elif query_type and not query_rating:
        reviews = BeerReview.objects.filter(creator=request.user
            ).filter(beertype__exact=query_type
            ).order_by('name')
        check_result()
    elif query_rating and not query_type:
        reviews = BeerReview.objects.filter(creator=request.user
            ).filter(rating__exact=query_rating
            ).order_by('name')
        check_result()

    return render(
        request,
        'diary/filter.html',
        context={'form': form, 'reviews': reviews},
    )