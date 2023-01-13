from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_up,name='sign'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass/',views.changepass,name='changepass'),
    path('changepass1/',views.changepass1,name='changepass1'),
    path('userdetail/<int:id>',views.user_detail,name='user_detail'),
    path('userdetail/',views.user_detail,name='user_detail'),
]