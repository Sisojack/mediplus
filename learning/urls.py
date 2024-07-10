from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('404/', views.notfound, name= '404'),
    path('blog-single/', views.blog, name= 'blog-single'),
    path('contact/', views.contact, name= 'contact'),
    path('portfolio/', views.portfolio, name= 'portfolio-details'),
    path('#/', views.ipnav)

]