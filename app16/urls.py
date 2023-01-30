from django.urls import path
from.import views
app_name='app16'
urlpatterns=[
    
    path('register/',views.register,name='register'),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('update/<int:id>',views.update,name='update'),
    path('home/<int:id>',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('gallery/<int:id>',views.gallery,name='gallery'),
    path('detail/<int:id>',views.detail,name='detail'),
]