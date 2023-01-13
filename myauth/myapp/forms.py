from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignupForm(UserCreationForm):
    #This is use to inherite the usercreation form
    password2= forms.CharField(label='Conform Password', widget=forms.PasswordInput())
    #  this is use  to change he password working
    class Meta:
        model = User
        # to inherite the user table 
        fields = ['username','first_name','first_name','last_name','email']
        # name the field to display in the table 
        labels ={'email': 'Email'}
        # to change the email name to Email Address to Email 


#creating new fields to showing the profile in user login
class EditUserProfileForm(UserChangeForm):      #inherting the userchange form and edit the fields
    password = None     #For not showing the password field
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels= {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):      #inherting the userchange form and edit the fields
    password = None     #For not showing the password field
    class Meta:
        model = User
        fields = '__all__'
        labels= {'email': 'Email'}