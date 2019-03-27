
from django.urls import path
from . import views

app_name ='bbs1'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('music/',views.MusicView.as_view(),name='music'),
    path('logout/',views.logout,name='logout'),
]