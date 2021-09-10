from rest_framework import routers, urlpatterns
from .viewset import *

router = routers.SimpleRouter()
router.register('',AlumnoViewset)
router.register('api/v1.0/matriculas',MatriculaViewset)

urlpatterns = router.urls