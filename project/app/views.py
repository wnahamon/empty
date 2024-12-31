from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm
# Create your views here.

def main(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})

def delete(request, id):
    
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('main')
    
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(
                title=form.cleaned_data['title'],
                price=form.cleaned_data['price'],
                desc=form.cleaned_data['desc'],
                category= form.cleaned_data['category']
            )
            product.save()
            return redirect('main')
    else:
        form = ProductForm()
        return render(request, 'create.html', {'form':form})


def read(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'read.html', {'product': product})

def update(request, id):
    product = Product.objects.get(id=id)
    title = product.title
    price = product.price
    desc = product.desc
    category = product.category
    if request.method =='POST':
            product.title = request.POST.get('title', title)
            product.price = request.POST.get('price', price)
            product.desc = request.POST.get('desc', desc)
            product.category = category
            product.save()
            return redirect('main')
    else:

        return render(request, 'update.html', {'product': product})