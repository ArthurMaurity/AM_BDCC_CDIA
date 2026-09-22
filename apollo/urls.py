from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

def healthcheck(_request):
    return JsonResponse({'status': 'ok'})

urlpatterns = [
    path('', healthcheck),  # Health check do EB retorna 200
    path('admin/', admin.site.urls),
    path('api/', include('avaliacoes.urls')),
]
