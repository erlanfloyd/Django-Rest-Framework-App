from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('University', views.UniversityView)
router.register('rectorat', views.RectoratView)
router.register('kafedra', views.kafedraView)
router.register('prorector', views.prorectorView)

urlpatterns = [
    url('', include(router.urls))   
]
