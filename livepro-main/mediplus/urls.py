from django.urls import path
from . import views
urlpatterns = [
    
path('', views.home, name='home'),
path('404', views.error, name='learn'),
path('blog', views.blog, name='login'),
path('portfolio', views.portfolio, name='login'),
path('contact', views.contact, name='login'),
path('homee', views.homee, name='home'),


]