from rest_framework import fields, serializers
from .models import *

class MatriculaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Matricula
      fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Alumno
      fields = '__all__'