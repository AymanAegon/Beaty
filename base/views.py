from datetime import datetime
from pyexpat import model
from django.shortcuts import render, redirect
from .models import Beat, Message, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MyUserCreationForm, BeatForm
from django.contrib.auth.decorators import login_required



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password incorrect!')
    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Oops, try again')
    context = {'form': form}
    return render(request, 'base/signup.html', context)

def home(request):
    beats = Beat.objects.all()
    context = {'beats': beats}

        

    return render(request, 'base/home.html', context)

def beat(request, pk):
    beats = Beat.objects.all()
    beat = Beat.objects.get(id=pk)
    chat = beat.message_set.all()
    if request.method == 'POST':
            mes = Message.objects.create(
                user = request.user,
                beat = beat,
                body = request.POST.get('body')
            )
            beat.updated = datetime.now()
            beat.save()
            # res.participants.add(request.user)
            return redirect('beat', pk=beat.id)

    context = {'beat': beat, 'chat': chat, 'beats': beats}
    return render(request, 'base/beat.html', context)

@login_required(login_url='login')
def create(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        creater = request.user
        beat = Beat.objects.create(name=name, creater=creater)
        return redirect('beat', pk=beat.id)
    context = {}
    return render(request, 'base/beat-form.html', context)

@login_required(login_url='login')
def deleteBeat(request, pk):
    beat = Beat.objects.get(id=pk)
    if request.user != beat.creater:
        return redirect('home')
    if request.method == 'POST':
        beat.delete()
        return redirect('home')
    context = {'beat': beat}
    return render(request, 'base/delete-beat.html', context)

@login_required(login_url='login')
def profile(request):
    beats = Beat.objects.all()
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('firstName')
        user.last_name = request.POST.get('lastName')
        user.bio = request.POST.get('bio')
        user.save()
        return redirect('home')
        
    context = {'beats': beats}
    return render(request, 'base/profile.html', context)