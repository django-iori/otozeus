from django.urls import path
from .views import *

urlpatterns = [
    path('demo/', DemoView.as_view()),
    path('delete/', DeleteView.as_view()),
    path('templates/', index_template, name='index_template'),
    path('test/', test, name='test'),
]