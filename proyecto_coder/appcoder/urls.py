from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('profesores/', profesores, name='Profesores'),
    path('entregables/', entregables, name='Entregables'),
    path('cursoformulario/', formulario_curso, name='Formulario'),
    path('buscarcurso/', buscarCurso, name='BusquedaCurso')
]
