from django.shortcuts import render, HttpResponse, Http404, redirect
from .forms import AddProductInfoForm
# Create your views here.
from .models import Product
import accounts
from accounts import urls


def product_list_view(request , *args , **kwargs):
    rest_query_set = Product.objects.all().order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_list_view_elec(request , *args , **kwargs):
    rest_query_set = Product.objects.filter(category__icontains = "electronic").order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_list_view_jobs(request , *args , **kwargs):
    rest_query_set = Product.objects.filter(category__icontains = "job").order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_list_view_others(request , *args , **kwargs):
    rest_query_set = Product.objects.filter(category__icontains = "other").order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_list_view_stationary(request , *args , **kwargs):
    rest_query_set = Product.objects.filter(category__icontains = "stationary").order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_list_view_roomdecor(request , *args , **kwargs):
    rest_query_set = Product.objects.filter(category__icontains = "roomdecor").order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_list_view_vehicles(request , *args , **kwargs):
    rest_query_set = Product.objects.filter(category__icontains = "vehicle").order_by('-date')
    context = {
        'object_list'     : rest_query_set 
    }
    return render(request, 'home.html',context)

def product_detail_view(request, slug, *args, **kwargs):
    query_set = Product.objects.filter(slug= slug)
    if  query_set.count()==1:
        instance = query_set.first()
        context = {
            'query_set' : instance
        }
    else:
        raise Http404("Oops!! We are unable to get the product..")
    return render(request,"product_detail.html",context )


def postad(request , *args , **kwargs):
    if request.user.is_authenticated:
        print(request.method)
        if(request.method=='POST'):
            form = AddProductInfoForm(request.POST, request.FILES)
            print("THe form is")
            print(form)
            print(form.is_valid())
            if form.is_valid():
                product_info=form.save(commit=False)
                print(product_info)
                product_info.seller_id=request.user
                print("COLLEGE")
                print(request.user.college_name)
                product_info.college = request.user.college_name
                print("PRODUCTINFO COLLEGE ")
                print(product_info.college)
                product_info.save()
                print(product_info)
                print("PRODUCTINFO COLLEGE ")
                print(product_info.college)
                print(request.user)
                print(request.method)
                return redirect('product:home')
        else:
            form=AddProductInfoForm()
        return render(request,'add_product.html',{'form':form})
    else:
        return redirect('accounts:login')