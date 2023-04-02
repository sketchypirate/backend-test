from django.views.generic.base import TemplateView
from django.urls import path, include
from .views import PlanetView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'planets', PlanetView, basename='planets')

urlpatterns = [
	path('', include(router.urls)),
]