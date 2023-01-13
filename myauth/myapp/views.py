from django.shortcuts import render,HttpResponseRedirect    #for redirect the page
from django.contrib.auth.forms import UserCreationForm      #including the user table
from .forms import SignupForm,EditUserProfileForm ,EditAdminProfileForm   
from django.contrib import messages   
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm ,SetPasswordForm  #including the login form
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash   #include for login to authencation and login and logout
from django.contrib.auth.models import User         #informting for diplaying the list of user

'''
all the data are available in in request.user we can fatch all the data realeated to the user
for example:
    request.user.username = it will factch the user name
    request.user.email = it fatch the email of the current user
'''

#signup view function
def sign_up(request):
    if request.method =='POST':
        fm = SignupForm(request.POST)
        # Featching the data and save into the fm object 
        if fm.is_valid():
            # validating the forms 
            fm.save()
            # save the form 
    else:
        # if the user come to get method itwill run this part 
        fm = SignupForm()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:         #if the user not lgin it will run
        if request.method =='POST':
            fm = AuthenticationForm(request=request, data=request.POST) # fatching the data from html
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                print(uname)                        #printing the informations...
                print(upass)
                user = authenticate(username=uname,password=upass)          #for varify the user available or not
                if user is not None:
                    login(request,user)             #if the user is present then login him
                    messages.success(request,'logged in sucessfully')
                    return HttpResponseRedirect('/profile/')        #must be start and end with slesh
            else:
                print('5')
                fm = AuthenticationForm()
                messages.success(request,'Password or Username incorrect')
                return render(request,'login.html',{'form':fm})
        else:
            fm = AuthenticationForm()                   #giving the login forn like username and password field
            return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


#Profile
def user_profile(request):
    if request.user.is_authenticated:       #its cheak the user is login
        if request.method == 'POST':
            if request.user.is_superuser == True:       # if user is admin it save the data in admin form
                fm = EditAdminProfileForm(request.POST, instance= request.user)
                users = User.objects.all()
            else: # else the data save in normal user form
                fm= EditUserProfileForm(request.POST,instance= request.user)
                users = None
            if fm.is_valid():
                messages.success(request,'Profile Update')
                fm.save()
        else:
            if request.user.is_superuser ==True:        #if the use is admin it return the admin form
                print("adminfghdfh")
                fm = EditAdminProfileForm(instance= request.user)
                users = User.objects.all()
                print(users)
            else:
                fm= EditUserProfileForm(instance= request.user)     #else return the user form
                users = None
            return render(request,'profile.html',{'name': request.user.first_name, 'form': fm, 'users':users})    #if login it run
    else:
        return HttpResponseRedirect('/login/')


#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
# change password with old Password
def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)   #when we change the pass it clear the session for mainting this
                #use use update_session_auth_hash function it update the session
                messages.success(request,"password change sucessfully")
                return HttpResponseRedirect('/profile/')
        fm = PasswordChangeForm(user=request.user)      #kis ka password change karna he
        return render(request,'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# change password without old Password
def changepass1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"password change sucessfully")
                return HttpResponseRedirect('/profile/')
        fm = SetPasswordForm(user=request.user)      #kis ka password change karna he
        return render(request,'changepass1.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditUserProfileForm(instance= pi)
        return render(request,'userdetails.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')