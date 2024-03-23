from django.http import JsonResponse
from bd.models import Gastos
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def select(request):
    # Realiza la suma de los registros del campo valor
    total_suma = Gastos.objects.aggregate(total_suma=Sum('valor'))

    # Accede al resultado de la suma
    resultado = total_suma['total_suma']
    
    # guarda el numero de la cantidad de registros
    total =  Gastos.objects.count()

    result = list(Gastos.objects.all().order_by("-fecha").values())
    return JsonResponse([resultado,result,total], safe=False)

def detalle_gasto(request, gasto_id):
        # Obtener el gasto específico por su ID
        gasto = list(Gastos.objects.filter(id=gasto_id).all().values())

        if gasto == []:
            return JsonResponse({'error': 'El gasto no existe'}, status=404)
        else:
            return JsonResponse(gasto, safe=False)


@csrf_exempt
def update(request):

    if request.method == 'POST':
        # actualiza los campos con los datos que llegan de la web        
        Gastos.objects.filter(id=request.POST.get('id')).update(nombre=request.POST.get('nombre'),descripcion=request.POST.get('descripcion'),valor=request.POST.get('valor'), fecha=request.POST.get('fecha'),categoria=request.POST.get('categoria'))
    
        result = {'info': f'Los datos de la persona han sido actualizados'}
        return JsonResponse(result)
    return JsonResponse({"error": "los datos de la persona no han sido actualizados"})
    

@csrf_exempt
def insert(request):

    if request.method == 'POST':
        # Inserta los campos con los datos que llegan de la web   
        Gastos.objects.create(nombre=request.POST.get('nombre'),descripcion=request.POST.get('descripcion'),valor=request.POST.get('valor'), fecha=request.POST.get('fecha'),categoria=request.POST.get('categoria'))

        data = {'info': "el usuario se a ingresado correctamente"}
        return JsonResponse(data,safe=False)
    
    return JsonResponse({"nada":"los datos de la persona no han sido ingresados"})

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        Gastos.objects.filter(id=request.POST.get('id')).delete()

        data = {'info': "el usuario se a elimninado correctamente"}

        return JsonResponse(data)
    return JsonResponse({})
    
def login(request):
    if request.method == 'POST':
        # Inserta los campos con los datos que llegan de la web   
        Gastos.objects.create(correo=request.POST.get('correo'),clave=request.POST.get('contra'))

        data = {'info': "el usuario se a ingresado correctamente"}
        return JsonResponse(data,safe=False)
    
    return JsonResponse({"nada":"los datos de la persona no han sido ingresados"})