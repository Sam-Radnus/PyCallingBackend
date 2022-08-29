from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('welcome',views.welcome,name="welcome message"),
    path('join',views.joinRoom,name="join room"),
    path('leave/<str:pk>',views.leaveRoom,name="leave room"),
    path('info/<str:sk>/<str:pk>',views.getParticipantInfo,name="leave room"),
]
