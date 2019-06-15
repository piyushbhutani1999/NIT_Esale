from django.urls import path
from . import views

app_name="accounts"


urlpatterns = [
    path('', views.HomePageView.as_view(), name= 'home'),
    path('signup/',views.register_user, name = 'signup'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('profile/', views.profile_view, name = 'profile'),
    path('aboutus/', views.AboutUsPageView.as_view(), name= 'aboutus'),
    path('contactus/', views.ContactUsPageView.as_view(), name= 'contactus'),
    path('profile/update/', views.update_user_profile, name= 'update_user_profile'),
    path('profile/update/phone', views.update_user_profile_phonenumber, name= 'update_user_profile_phonenumber'),
    path('profile/myad/', views.my_ads_view, name = 'myads'),
    path('profile/myad/editad/<str:slug>', views.edit_product, name = 'editad'),
  

]
