from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from .models import User
from .forms import LoginForm,UserRegisterForm,UserEditForm,UserPhoneEditForm
from django.views.generic import TemplateView
from product.models import Product
from django.contrib import messages
from product.forms import AddProductInfoForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsPageView(TemplateView):
    template_name = 'aboutus.html'


class ContactUsPageView(TemplateView):
    template_name = 'contactus.html'


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
                return redirect('product:home')


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
        print(form)
        print(form.is_valid())
        if form.is_valid():
            password_ = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            college_name = form.cleaned_data['college_name']
            user = User.objects.create_user(email=email, password=password_, first_name=first_name, last_name=last_name , phone=phone, college_name = college_name)
            user.save()
            return redirect('product:home')
    else:
        form = UserRegisterForm()
    return render(request,'signup.html',{'form':form})

def profile_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{})
    else:
        return redirect('accounts:login')

def update_user_profile(request):
    if request.user.is_authenticated:
        phone = request.user.phone
        first_name = request.user.first_name
        last_name = request.user.last_name
        print(request.method)
        if request.method == 'POST':
            form = UserEditForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                user_info = request.user
                user_info.first_name = form.cleaned_data['first_name']
                user_info.last_name = form.cleaned_data['last_name']
                new_phone = form.cleaned_data['phone']
                if new_phone!=phone:
                    phone_list = User.objects.all()
                    print(phone_list)
                    for x in phone_list:
                        if new_phone == x.phone:
                            messages.error(request, 'Phone Number already exists.')
                            return render(request, 'update.html', {'form': form})
                request.user.phone = new_phone
                try:
                    request.user.save()
                except:
                    return render(request, 'update.html', {'form': form})
                return redirect('accounts:profile')
            
        else:
            form = UserEditForm(initial={'phone':phone, 'first_name':first_name , 'last_name':last_name})
        return render(request, 'update.html', {'form': form})
    else:
        return redirect('accounts:login')

def update_user_profile_phonenumber(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserPhoneEditForm(request.POST)
            print(form)
            old_phone= form.cleaned_data['old_phone']
            confirm_phone = form.cleaned_data['confirm_phone']
            new_phone =form.cleaned_data['new_phone']
            phone = request.user.phone
            if old_phone != phone:
                raise ValueError("old phonenumber is not correct")
            print(old_phone)
            if confirm_phone != new_phone:
                raise ValueError("confirm phone doesnot match")
            
            print(confirm_phone)
            print("CHECK VALIDITY")
            print(form.is_valid)
            user = request.user
            user.phone = confirm_phone
            print("dekh error aya koi")
            print(request.user.phone)
            try:
                user.save()
            except:
                raise ValueError("please enter a nonused number")
            print(new_phone)
            return redirect('product:home')
        else:
            form = UserPhoneEditForm()
        return render(request, 'update2.html', {'form': form})
    else:
        return redirect('accounts:login')


def my_ads_view(request):
    if request.user.is_authenticated:
        instance = Product.objects.filter(seller_id = request.user.pk)
        context = {
            'query_set' : instance
        }
        return render(request,"my_ads.html",context )
    else:
        return redirect('accounts:login')


def edit_product(request,slug):
    if request.user.is_authenticated:
        obj = Product.objects.filter(slug = slug , seller_id = request.user.pk)
        print("THE OBJECT IS")
        print(obj)
        if obj.count()==1:
            obj = obj.first()
            print(obj)
            title = obj.title
            description = obj.description
            price = obj.price
            image = obj.image
            print(title)
            print(description)
            print(image)
            print("the object image is")
            print(obj.image)
            category = obj.category
            if request.method =='POST':
                form = AddProductInfoForm(request.POST ,request.FILES)
                print("THE FORM IS")
                print(form)
                if form.is_valid():
                    new_price = form.cleaned_data['price']
                    new_title = form.cleaned_data['title']
                    new_description = form.cleaned_data['description']
                    new_image = form.cleaned_data['image']
                    new_category = form.cleaned_data['category']
                    obj.title = new_title
                    obj.price = new_price
                    obj.description = new_description
                    obj.image = new_image
                    obj.category = new_category
                    print("the new image is")
                    print(obj.image)
                    print(obj)
                    try: 
                        obj.save()
                    except:
                        return render(request, 'update_ad.html', {'form': form})
                    return redirect('product:home')
            
            else:
                form = AddProductInfoForm(initial={'title':title, 'description':description , 'category':category,'price':price, 'image':image})
                print("THE DEFAULT IMAGE IS:")
                print(obj.image)
                print(form)
            return render(request, 'update_ad.html', {'form': form})
        else:
            raise ValueError("The product is not associated to the authenticated user")
        # else:
        #     raise ValueError("not find product for such slug.You should again login and try on that side")
    else:
        return redirect('accounts:login')
            
                            
 




def logout_view(request):
    logout(request)
    return redirect('product:home')