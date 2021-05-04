from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
]

# Создает URL-путь к index.html через функцию index() в views.py и к каждой записи в BeerReview
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^beers/$', views.BeerReviewListView.as_view(), name='beers'),
    url(r'^beer/(?P<pk>\d+)$', views.BeerReviewDetailView.as_view(), name='beer-detail'),
]

# Создает путь к обзорам с наивысшим рейтингом залогиненного пользователя
urlpatterns += [
    url(r'^myperfectbeers/$', views.PefectBeerReviewsByUserListView.as_view(), name='my-perfect-beers'),
]