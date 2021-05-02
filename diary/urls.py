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
]