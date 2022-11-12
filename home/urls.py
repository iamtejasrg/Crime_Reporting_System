from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    path("aboutus", views.aboutus, name='aboutus'), 
    path("helpline", views.helpline, name='helpline'), 
    path("safety", views.safety, name='safety'), 
    path("login", views.login, name='login'), 
    
    path("signup", views.signup, name='signup'),
    path("contact", views.contact, name='contact'), 
    path("complaint", views.complaint, name='complaint'), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)