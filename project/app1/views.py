from urllib.robotparser import RequestRate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import register
from django.urls import reverse

# Create your views here.
def a(request):
    return HttpResponse("wee")

def dashbord_view(request):
    if 'email' in request.session:
        profile_name = request.session['email']
        user_data = register.objects.get(user_email = profile_name)
    else:
        return redirect('login')
        
    return render(request,'dashbord.html',{'p':profile_name,'user_info':user_data})

def logout(request):
    if request.session.has_key('email'):
        a = request.session['email']
        print(a)
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')

def login_view(request):
    if request.method=='POST':
        try:
            email  = request.POST['email']
            password = request.POST['password']
            user  = register.objects.get(user_email=email)
            # print(user)
            if user.user_password1 == password:
                request.session['email'] = email
                a = request.session['email']
                print(a)
                print('login')
                return redirect('dashbord')
            else:
                return render(request,'login.html',{'msg':'wrong user password '})
        except:
            return render(request,'login.html',{'msg':'wrong user email '})
    return render(request,'login.html')



def register_view(request):
    if request.method=='POST':
        user = register()
        user.user_name = request.POST['user_name']
        user.user_email = request.POST['user_email']
        user.user_dob = request.POST['user_dob']
        user.user_phone_no =request.POST['user_number']
        user.user_password1 = request.POST['user_password1']
        user.user_password2 = request.POST['user_password2']
        if user.user_password1==user.user_password2:
            user.save()
            return redirect('login')
            
        else:
            error = "password is diffrent "
            return render(request,'register.html',{'error':error})
    return render(request,'register.html')


