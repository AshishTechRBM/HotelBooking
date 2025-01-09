from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
         return redirect('/login')
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is home page")

def about(request):
    if request.user.is_anonymous:
         return redirect('/login')
    return render(request, 'about.html')

def services(request):
      if request.user.is_anonymous:
         return redirect('/login')
      return render(request, 'services.html')

def contact(request):
      if request.user.is_anonymous:
         return redirect('/login')
      if request.method == 'POST':
           username = request.POST.get('username')
           email = request.POST.get('email')
           phone = request.POST.get('phone')
           desc = request.POST.get('desc')
           contact = Contact(username = username,email=email,phone=phone,desc=desc,date=datetime.today())
           contact.save()
           messages.success(request, "Your message has been send!")
      return render(request, 'contact.html')

def loginUser(request):
     if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(username=username, password=password)
          if user is not None:
              login(request,user)
              return redirect('/')
          else:
              return render(request, 'login.html')
          
     return render(request, 'login.html')

def logoutUser(request):
     logout(request)
     return redirect('/login')