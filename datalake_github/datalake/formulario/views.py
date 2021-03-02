from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormularioBase
from .models import CallesCondiciones, Paises
from django.http import JsonResponse

@login_required
def formulario(request):
    
    if request.method == 'POST':
        fb_form = FormularioBase(request.POST)
        if fb_form.is_valid():
            fb_form.save()
            messages.success(request, f'El formulario se subio correctamente')
            return redirect('core-home')
    else:
        fb_form = FormularioBase()

    context = {
        'fb_form': fb_form,
    }
    return render(request, 'formulario/formulario1.html', context) 

def autocompete_calles(request):
    if 'term' in request.GET:
        qs = CallesCondiciones.objects.filter(calle__contains=request.GET.get('term'))
        calles = list()
        for calle in qs:
            calles.append(calle.calle)
        return JsonResponse(calles, safe=False)

def autocompete_pais(request):  
    if 'term' in request.GET:
        qs = Paises.objects.filter(nombre__contains=request.GET.get('term'))
        paises = list()
        for pais in qs:
            paises.append(pais.nombre)
        return JsonResponse(paises, safe=False)



