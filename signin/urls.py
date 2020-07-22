
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from signin import views


urlpatterns = [
    path('users/', views.Users.as_view(), name='users'),
    path('details/<int:pk>', views.UserDetail.as_view(), name='profile')
]

urlpatterns = format_suffix_patterns(urlpatterns)
