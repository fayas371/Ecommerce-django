from django.urls import path

from .import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.dashboard,name='dashboard'),
    path('account/<uidb64>/<token>/',views.activate,name='activate'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),
    path('myorders',views.myorders,name='myorders'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('change_password',views.change_password,name='change_password'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('contact_us',views.contact_us,name='contact_us'),
    
]