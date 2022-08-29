from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('welcome',views.welcome,name="welcome message")
]
