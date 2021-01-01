import africastalking
from django.shortcuts import render
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#login
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

username ="byusagisele@gmail.com"
api_key = "fadcb6a9ccf85104850af3477cc74d46eb392efb4940ff37495b8db395fa2e14"
africastalking.initialize(username, api_key)
# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username,
            'first_name':user.first_name,
        })
def welcome(request):
    return render(request, 'index.html')


def index(request):
    data = Gallery.objects.all

    return render(request, "index.html", {'all': data})
    

