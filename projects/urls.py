from pkgutil import ImpLoader
from rest_framework import routers
from .api import ProjectViewSet


router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls   #con esto se generan las urls necesarias
