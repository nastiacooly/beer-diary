from django.urls import path
from . import views
from django.conf.urls import url

# Создает URL-путь к index.html через функцию index() в views.py и к каждой записи в BeerReview
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^beers/$', views.BeerReviewListView.as_view(), name='beers'),
    url(r'^beer/(?P<pk>\d+)$', views.BeerReviewDetailView.as_view(), name='beer-detail'),
]

urlpatterns += [
    url(r'^search/$', views.beer_search, name="search"),
    url(r'^filter/$', views.beers_filter, name="filter"),
]

# Создает путь к обзорам с наивысшим рейтингом залогиненного пользователя
urlpatterns += [
    url(r'^myperfectbeers/$', views.PefectBeerReviewsByUserListView.as_view(), name='my-perfect-beers'),
]

# Создает путь к форме обновления обзора
urlpatterns += [
    url(r'^beer/(?P<pk>\d+)/update/$', views.update_beer_review, name='update_beer_review'),
]

# Создает путь к форме добавления обзора
urlpatterns += [
    url(r'^beer/create/$', views.add_new_beer_review, name='add_new_beer_review'),
]

# Создает путь к удалению обзора
urlpatterns += [
    url(r'^beer/(?P<pk>\d+)/delete/$', views.delete_beer_review, name='delete_beer_review'),
]