from django.urls import path
from basic import views

app_name = 'basic'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.registration,name='registration'),
    path('logout/',views.user_Logout,name='Logout'),
    path('login/',views.user_Login,name='Login'),
    path('special/',views.special,name='special'),


]
