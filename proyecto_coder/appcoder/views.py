from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import *
from appcoder.forms import *



# Create your views here.
def inicio(request):
    dict_ctx={'title':'Inicio','message':'Bienvenido al blog de Maru...'}
    return render(request, 'appcoder/index.html', dict_ctx)


def cursos(request):
    return render(request, 'appcoder/cursos.html')


def estudiantes(request):
    return render(request, 'appcoder/estudiantes.html')


def profesores(request):
    return render(request, 'appcoder/profesores.html')


def entregables(request):
    return render(request, 'appcoder/entregables.html')


def formulario_curso(request):
    if request.method=='POST':
        curso=CursoFormulario(request.POST)
        if curso.is_valid:
            data=curso.data
            curso_nuevo=Curso(nombre=data['nombre'], camada=data['camada'])
            curso_nuevo.save()
            return render(request, 'appcoder/index.html')
    else:
        curso_form=CursoFormulario()
        return render(request, 'appcoder/cursoFormulario.html', {'formulario':curso_form})


def buscarCurso(request):
    data=request.GET['camada']
    if data:
        curso=Curso.objects.filter(camada=data)
        return render(request, 'appcoder/busquedaCurso.html', {'curso':curso})
    return render(request, 'appcoder/busquedaCurso.html')