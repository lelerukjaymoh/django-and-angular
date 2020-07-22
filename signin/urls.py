
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from signin import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/users/', views.Users.as_view(), name='users'),
    path('api/details/<int:pk>', views.UserDetail.as_view(), name='profile')
]

urlpatterns = format_suffix_patterns(urlpatterns)
