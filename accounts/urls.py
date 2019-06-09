from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name= 'home'),
    path('signup/',views.register_user, name = 'signup'),
    path('login/', views.login_user, name = 'login'),
    path('profile/', views.profile_view, name = 'profile'),
    path('aboutus/', views.AboutUsPageView.as_view(), name= 'aboutus')
  

]
