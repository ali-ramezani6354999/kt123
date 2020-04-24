
from django.conf.urls import url
from django.urls import path
import app1
from app1 import views






app_name='app1'

urlpatterns= [
    url(r'^$', views.Index.as_view() , name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
