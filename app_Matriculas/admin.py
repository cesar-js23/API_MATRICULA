from django.contrib import admin
from .models import Alumno, Matricula
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
   list_display = (
     'nombre', 'apellido', 'telefono', 'correo', 'direccion', 'foto_alumno'
   )
class MatriculaoAdmin(admin.ModelAdmin):
   list_display = (
     'fk_alumno', 'codigo', 'tipo', 'fecha', 'curso', 'carrera' 
   )




admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Matricula,MatriculaoAdmin)



