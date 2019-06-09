from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from .models import User
from .forms import LoginForm,UserRegisterForm
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsPageView(TemplateView):
    template_name = 'aboutus.html'

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # try:
                #     user_info = UserInfo.objects.get(user_id=user.pk)
                # except UserInfo.DoesNotExist:
                #     user_info = None

                # if user_info is not None:
                #     contacts_created = 1
                # else:
                #     contacts_created = 0
                # qs2 = User.objects.filter(is_active = True)
                # print("ACTIVE USERS     ")
                # print(qs2)
                return render(request,'home.html',{})


                # return redirect('home', pk=user.pk)
            else:
                messages.error(request, 'Incorrect Username or Password')
    else:
        form = LoginForm()
    # qs = User.objects.all()
    # print("NONNNNNNNACTIVE USERS     ")
    # print(qs)
    # qs2 = User.objects.filter(active = True)
    # print(qs2)
    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password_ = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create_user(email=email, password=password_, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'signup.html',{'form':form})

def profile_view(request, *args, **kwargs):
    qs = request.user
    qs = qs.product_set.all()
    context = {
        'product_list':qs
    }
    return render(request, 'profile.html',context)