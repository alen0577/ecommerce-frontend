from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')   

def home(request):
    return render(request,'home.html')
         
def fashionpage(request):
    return render(request,'fashion.html')    

def product_view(request):
    return render(request, 'product_view.html')   

def cart(request):
    return render(request, 'cart.html')   
