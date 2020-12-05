from django.shortcuts import render,redirect
from django.http import HttpResponse
from tech.form import ShopForm,hopForm
from tech.models import MyData , ShopData 
 


def myapp(request):
    if request.method == "POST":
        form =  ShopForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('tandu')
    else:
        return render(request,"base.html")


def app(request):
    if request.method == "POST":
        form =  hopForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('tandu')
    else:
        return render(request,"contact.html")
            

def tandu(request):
    return render(request, "ex.html")

def price(request):
    return render(request, "price.html")    