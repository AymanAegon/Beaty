from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('beat/<str:pk>/', views.beat, name="beat"),
    path('beat/<str:pk>/info', views.beatInfo, name="beat-info"),
    path('profile/<str:un>/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('join/<str:pk>/', views.joinBeat, name='join-beat'),
    path('exit/<str:pk>/', views.exitBeat, name='exit-beat'),
    path('delete/<str:pk>/', views.deleteBeat, name='delete-beat'),
    path('edit/<str:pk>/', views.editBeat, name='edit-beat'),
    path('delete-msg/<str:pk>/', views.deleteMsg, name='delete-msg'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupPage, name='signup')
]
