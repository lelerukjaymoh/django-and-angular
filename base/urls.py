from django.urls import include, path
from signin import views

urlpatterns = [
    path('api/', include('signin.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
