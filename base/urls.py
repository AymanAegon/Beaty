from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('beat/<str:pk>/', views.beat, name="beat"),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('delete/<str:pk>/', views.deleteBeat, name='delete-beat'),
    path('delete-msg/<str:pk>/', views.deleteMsg, name='delete-msg'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupPage, name='signup')
]
