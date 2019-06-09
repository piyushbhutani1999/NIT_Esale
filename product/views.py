from django.shortcuts import render, HttpResponse, Http404, redirect
from .forms import AddProductInfoForm
# Create your views here.
from .models import Product


def product_list_view(request , *args , **kwargs):
    featured_query_set = Product.objects.filter(featured = True)
    rest_query_set = Product.objects.filter(featured = False)
    context = {
        'featured_object_list' : featured_query_set,
        'rest_object_list'     : rest_query_set 
    }
    return render(request, 'product_list.html',context)

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


def add_product(request , *args , **kwargs):
    print(args)
    print(kwargs)
    print(request.user)
    print(request.method)
    if(request.method=='POST'):
        form = AddProductInfoForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            product_info=form.save(commit=False)
            print(product_info)
            product_info.seller_id=request.user
            product_info.save()
            print(request.user)
            print(request.method)
            return redirect('home')
    else:
        form=AddProductInfoForm()
    return render(request,'add_product.html',{'form':form})