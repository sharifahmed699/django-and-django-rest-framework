from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop, Phone
from .forms import LaptopForm,PhoneForm

# Create your views here.
def index(request):
	return render(request, "index.html")

def laptop(request):
	items=Laptop.objects.all()
	context={
		'items':items,
		'title':"Laptop"
	}
	return render(request, "index.html", context)


def phone(request):
	items=Phone.objects.all()
	context={
		'items':items,
		'title':"Phone"
	}
	return render(request, "index.html", context)


def insert(request, abc):
	if request.method=="POST":
		form=abc(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=abc()
		return render(request,"insert.html",{'form':form})
def insert_laptop(request):
	return insert(request, LaptopForm)

def insert_phone(request):
	return insert(request, PhoneForm)



def update(request, pk, key, abc):  
	item=get_object_or_404(key, pk=pk)
	if request.method=="POST":
		form = abc(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=abc(instance=item)
		return render(request,"update.html",{'form':form})
   
def update_laptop(request, pk):
	return update(request, pk, Laptop, LaptopForm)
def update_phone(request, pk):
	return update(request, pk, Phone, PhoneForm)


def laptop_delete(request, pk):  
    laptop = Laptop.objects.get(pk=pk)  
    laptop.delete()  
    return redirect('Laptop')  

def phone_delete(request, pk):  
    phone = Phone.objects.get(pk=pk)  
    phone.delete()  
    return redirect('Phone')  