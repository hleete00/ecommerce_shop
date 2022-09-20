from django.urls import path
from . import views

app_name = 'core'


def test():
    a = b
    b = 5


urlpatterns = [
    path('', views.item_list, name='item-list')
]
