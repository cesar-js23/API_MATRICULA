
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

def url(self,filename):
   ruta = "static/img/alumno/%s/%s"%(self.nombre,str(filename))
   return ruta

class Alumno(models.Model):

   def foto_alumno(self):
      return mark_safe('<a href="/%s"> <img src="/%s" with="50px" height="50px"/> </a>'%(self.foto,self.foto))


   nombre = models.CharField(max_length=45, blank=False)
   apellido = models.CharField(max_length=45, blank=False)
   telefono = models.IntegerField(blank=False)
   correo = models.EmailField(blank=False)
   direccion = models.CharField(max_length=100, blank=False)
   foto = models.ImageField(upload_to=url)

   def __str__(self):
       return f'{self.nombre} {self.apellido} '

tipo_matricula =[
  ('ORDINARIA','ORDINARIA'),
  ('EXTRAORDINARIA','EXTRAORDINARIA'),
  ('ESPECIAL','ESPECIAL'),
]

tipo_curso =[
  ('1','I CICLO'),
  ('2','II CICLO'),
  ('3','III CICLO'),
  ('4','Iv CICLO'),
  ('5','v CICLO'),
]


class Matricula(models.Model):
   codigo = models.CharField(max_length=8, blank=False)
   tipo = models.CharField(max_length=45,choices=tipo_matricula,default='available')
   fecha = models.DateField(blank=False)
   curso = models.CharField(max_length=45,choices=tipo_curso,default='available')
   carrera = models.CharField(max_length=100, blank=False)
   fk_alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, blank=False)

   def __str__(self):
       return self.tipo