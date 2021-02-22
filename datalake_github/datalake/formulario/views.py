from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormularioBase

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
