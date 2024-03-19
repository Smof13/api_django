from django.shortcuts import render
from django.http import JsonResponse
from bd.models import Gastos
from datetime import datetime
from django.db.models import Sum


# Create your views here.

from django.views.decorators.csrf import csrf_exempt

def select(request):
    # Realiza la suma usando el ORM de Django
    total_suma = Gastos.objects.aggregate(total_suma=Sum('valor'))

    # Accede al resultado de la suma
    resultado = total_suma['total_suma']
    total =  Gastos.objects.count()
    # Gastos.objects.create(nombre="pago salario",descripcion="la quincena", valor=487500,fecha="2024-03-18",categoria="sueldo")
    result = list(Gastos.objects.all().values())
    return JsonResponse([resultado,result,total], safe=False)

def update(request):

    if request.method == 'POST':
        firstUser = Gastos.objects.get(id=request.POST.get('id'))
        
        Gastos.objects.filter(id=request.POST.get('id')).update(nombre=request.POST.get('nombre'),descripcion=request.POST.get('descripcion'),valor=request.POST.get('valor'), fecha=request.POST.get('fecha'),categoria=request.POST.get('categoria'))

        # lastUser = Gastos.objects.get(id=request.POST.get('id'))

        
        result = {'info': f'Los datos de la persona {firstUser.id} han sido actualizados'}
        return JsonResponse(result)
    return JsonResponse()
    

@csrf_exempt
def insert(request):

    if request.method == 'POST':
        Gastos.objects.create(nombre=request.POST.get('nombre'),descripcion=request.POST.get('descripcion'),valor=request.POST.get('valor'), fecha=request.POST.get('fecha'),categoria=request.POST.get('categoria'))
        data = {'info': "el usuario se a ingresado correctamente"}
        return JsonResponse(data,safe=False)
    
    return JsonResponse({"nada":"nada"})

def delete(request):
    if request.method == 'POST':
        Gastos.objects.filter(id=request.POST.get('id')).delete()

        data = {'info': "el usuario se a elimninado correctamente"}

        return JsonResponse(data)
    return JsonResponse()
    
