from django.urls import include, path
from .views import AlunoViewSet, AvaliacaoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
