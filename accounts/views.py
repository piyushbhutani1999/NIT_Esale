from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from .models import User
from .forms import LoginForm,UserRegisterForm,UserEditForm
from django.views.generic import TemplateView
from product.models import Product
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
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'signup.html',{'form':form})

def profile_view(request, *args, **kwargs):
    return render(request, 'profile.html',{})

def update_user_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        print(form)
        if form.is_valid():
            user_info = request.user
            user_info.first_name = form.cleaned_data['first_name']
            user_info.last_name = form.cleaned_data['last_name']
            print(user_info)
            user_info.save()
            print(user_info)
            return redirect('home')
    else:
        form = UserEditForm()
    return render(request, 'update.html', {'form': form})

def my_ads_view(request):
    print(request.user)
    instance = Product.objects.filter(seller_id = request.user.pk)
    print(instance)
    context = {
            'query_set' : instance
        }
    return render(request,"my_ads.html",context )
# def edit_product(request,slug):
#     form_class = AddProductInfoForm
#     form = form_class(request.POST or request.files or None)
#     print(form)
#     product=Product.objects.get(slug = slug)
#     print(product)
#     print(form.is_valid())    
#     print(form)
#     # if request.user.id!= product.seller_id:
#     #     raise HttpResponse("sorry!! user is not athenticated yet")
#     if request.method=='POST':
#         if form.is_valid():
#             product.title=form.cleaned_data['title']
#             product.description = form.changed_data['description']
#             product.price=form.cleaned_data['price']
#             product.image = form.cleaned_data['image']
#             print(product)
#             product.save()
#             return redirect('home')

#     # else:
#     #     title=form.cleaned_data['title']
#     #     description = form.changed_data['description']
#     #     price=form.cleaned_data['price']
#     #     image = form.cleaned_data['image']

#     #     default_data={'title':title,'price':price,'image':image,'description':description}
#     #     form=AddProductInfoForm(default_data)
#     return render(request, 'edit_product.html', {'form': form})
#     product = get_object_or_404(Product, slug=slug)
#     form = CustomerForm(request.POST or None, instance=product)
#     context = {"customerform": form,
#                "form_url": reverse_lazy('customer:edit'),
#                "type":"edit"
#                }
#     if request.method == "POST":
#         # print("success")
#         if form.is_valid():
#             f = form.save()
#             f.account_no = f.acc_no()
#             f.save()
#             return HttpResponseRedirect(reverse('customer:index'))
#     return render(request, "register.html", context)




def logout_view(request):
    logout(request)
    return redirect('product:home')