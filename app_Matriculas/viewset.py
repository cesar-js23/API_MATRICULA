from rest_framework import viewsets
from .serializer import *
from .models import *

class MatriculaViewset(viewsets.ModelViewSet):
   queryset = Matricula.objects.all()
   serializer_class = MatriculaSerializer



class AlumnoViewset(viewsets.ModelViewSet):
   queryset = Alumno.objects.all()
   serializer_class = AlumnoSerializer