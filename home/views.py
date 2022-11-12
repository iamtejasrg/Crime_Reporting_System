from django.shortcuts import HttpResponse, redirect, render
from datetime import datetime
from home.models import Contact, Signup, Login, Complaint
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def aboutus(request):
    return render(request, 'aboutus.html')

def helpline(request):
    return render(request, 'helpline.html')

def safety(request):
    return render(request, 'safety.html')


# def login(request):
#     if request.method =="POST":
#         uname = request.POST.get('uname')
#         psw= request.POST.get('psw')
#         login= Login(uname=uname, psw=psw)
#         login.save()
#         messages.success(request, 'You made it! Your account is created')
        
#     return render(request, 'complaint.html')
 
def login(request):
    if request.method =="POST":
        uname = request.POST.get('uname')
        psw= request.POST.get('psw')
        user= authenticate(usernname=uname, password=psw)
       
        if user is None:
            # login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/complaint")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")

    
    return render(request, 'login.html')


def signup(request):
    if request.method =="POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        add= request.POST.get('add')
        file = request.FILES.get('file')
        pwd=request.POST.get('pwd')
        rpwd=request.POST.get('rpwd')
        signup = Signup(name=name, surname=surname, phone=phone, email=email, add=add, file=file, pwd=pwd, rpwd=rpwd)
        signup.save()
        messages.success(request, 'You made it! Your account is created')
        
    return render(request, 'signup.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 

def complaint(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # BullyingType = request.POST.get('BullyingType')
        # ResultInInjury = request.POST.get('ResultInInjury')
        # BullyBehaviors = request.POST.get('BullyBehaviors')
        place= request.POST.get('place')
        Description=request.POST.get('Description')
        PhysicalEvidence=request.POST.get('PhysicalEvidence')
        fileUpload = request.FILES.get('fileUpload')
        complaint = Complaint(name=name,  place=place, Description=Description, PhysicalEvidence=PhysicalEvidence, fileUpload=fileUpload)
        complaint.save()
        messages.success(request, 'You made it! Your issue is reported')
        
    return render(request, 'complaint.html')
    
