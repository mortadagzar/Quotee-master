from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from QuoteeApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


app_name='QuoteeApp'

urlpatterns = [
    path('Quote', views.Quote, name='Quote'),
    path('register', views.register, name='register'),
    path('admin/', admin.site.urls,name='admin'),
    path('',views.index,name='index'),
    path('addquote',views.addquote,name='addquote'),
    path('registrations',views.registrations,name="registrations"),
    path('login',views.login,name='login'),
    path('logmein_p',views.logmein_p),
    path('feedback',views.feedback,name='feedback'),
    path('thanks',views.thanks,name='thanks'),
    path('success',views.success,name='success'),
    path('logmeout_p',views.logmeout_p,name='logmeout_p'),
    
     ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  
