from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def ProductDetailView(request):
    Obj = Product.objects.get(id=1)
    Context = {
    #    "Title"         : Obj.title,
    #    "Description"   : Obj.description
        "Object"        : Obj
    } 
    return render(request, "product/detail.html", {})

def ProductCreateView(request):
    print(request.GET)
    print(request.POST)
    Title = request.POST.get('Title')
    Context = {}
    return render(request, "products/product_create.html", Context)



    #Form = ProductForm(request.POST or None)
    #if Form.is_valid():
    #    Form.save()
    #    Form. ProductForm()

    #Obj = Product.objects.get(id=1)
    #Context = {
    #    'Form' : Form
    #} 
    #return render(request, "product/product_create.html", Context)
