from django.urls import path
from . import views

urlpatterns = [
    path('select/',views.select),
    path('update/',views.select),
    path('delete/',views.delete),
    path('insert/',views.insert),
]