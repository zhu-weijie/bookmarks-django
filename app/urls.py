from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:bookmark>/',
         views.bookmark_detail,
         name='bookmark_detail'),
]
