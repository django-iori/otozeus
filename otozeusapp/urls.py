from django.urls import path
from .views import *

urlpatterns = [
    path('upload_from_ios/', UploadFromIOS.as_view()),
    path('delete/', DeleteView.as_view()),
    path('templates/', index_template, name='index_template'),
    path('test/', test, name='test'),
]