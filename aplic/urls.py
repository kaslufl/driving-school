from django.urls import path, include
from .api.v1.router import router as v1
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/', include(v1.urls)),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
