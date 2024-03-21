from django.urls import path
from . import views

urlpatterns = [
    path('select/',views.select),
    path('detalle/<int:gasto_id>/',views.detalle_gasto),
    path('update/',views.select),
    path('delete/',views.delete),
    path('insert/',views.insert),
]