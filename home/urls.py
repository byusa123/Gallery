from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('',views.welcome, name='home'),
    
  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
