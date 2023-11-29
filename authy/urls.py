
from django.urls import path
from . import views
from .views import contact, success

urlpatterns = [
              path('login/', views.sign_in, name='login'),
              path('logout/', views.log_out, name='logout'),
              path('register/',views.sign_up,name='register'),
              path('home/',views.home,name='home'),
              path('about_us/',views.about_us,name='about_us'),
              path('privacy/',views.privacy,name='privacy'),
              path('dashboard/',views.dashboard,name='dashboard'),
              path('result/',views.result,name='result'),
              path('position/', views.position, name='position'),
              path('candidate/<int:pos>/', views.candidate, name='candidate'),
              path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
              path('contact/', contact, name='contact'),
              path('success/', success, name='success')


                ]