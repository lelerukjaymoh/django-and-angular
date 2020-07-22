from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from signin.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class Users(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'all_users.html'

    def get(self, request):
        users = User.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(users, context=serializer_context)
        return Response({'users': users})


class UserDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(user, context=serializer_context)
        return Response({'serializer': serializer, 'profile': user})

    def post(self, request, pk):
        print(pk)
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': user})
        serializer.save()
        return redirect('profile', pk=user.pk)

def home(request):
    return render(request, 'index.html', {})