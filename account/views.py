from django.shortcuts import render,redirect,HttpResponse
from .models import MyUser
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        print('hello')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email =  request.POST['email']
        password =  request.POST['password']
        c_password = request.POST['confirm_password']
        phone_number = request.POST['phone_number']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        if (password == c_password):
            print('sucess')
            user = MyUser.objects.create_user(
                                             first_name=first_name,
                                             last_name=last_name,
                                             email=email,
                                             password=password,
                                             phonenumber=phone_number,
                                             date_of_birth=date_of_birth,
                                             Gender=gender
                                             )
            user.save()
            print('user created')
            messages.info(request,"you have created a new account")
            return redirect(login)
        else:
           messages.info(request,"password does not match")
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
            email =  request.POST['email']
            print('email')
            password =  request.POST['password']
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                auth_login(request,user)
                print("logged in user")
                messages.info(request,"you have logged in succesfully")
                return render(request, 'home.html')
            else:
                print('why')
                messages.info(request,"username or password incorrect")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(login)

def home(request):
    