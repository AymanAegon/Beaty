from datetime import datetime
from django.shortcuts import render, redirect
from .models import Beat, Message, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .forms import EditBeat, MyUserCreationForm, EditUser
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
            
    context = {'form': form}
    return render(request, 'base/signup.html', context)

@login_required(login_url='login')
def home(request):
    search = request.GET.get('search') if request.GET.get('search') else ''
    beats = request.user.beat_set.filter(
        Q(name__icontains=search) |
        Q(creater__username__icontains=search) |
        Q(description__icontains=search)
        )
    if len(beats)==0:
        beats=None
    context = {'beats': beats, 'search': search}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def beat(request, pk):
    search = request.GET.get('search') if request.GET.get('search') else ''
    beats = request.user.beat_set.filter(
        Q(name__icontains=search) |
        Q(creater__username__icontains=search) |
        Q(description__icontains=search)
        )
    if len(beats)==0:
        beats=None
    try:
        beat = Beat.objects.get(id=pk)
    except Beat.DoesNotExist:
        return redirect('home')
    
    user = beat.members.filter(id=request.user.id)
    if len(user)==0:
        return redirect('join-beat', pk=beat.id)
    chat = beat.message_set.all()

    if request.method == 'POST':
        if 'delete_msg' in request.POST:
            i = int(request.POST.get('input_msg_id'))
            msg = Message.objects.get(id=i)
            msg.delete()
            return redirect('beat', pk=msg.beat.id)
        else:
            mes = Message.objects.create(
                user = request.user,
                beat = beat,
                body = request.POST.get('body')
            )
            beat.updated = datetime.now()
            beat.save()
            return redirect('beat', pk=beat.id)

    context = {'beat': beat,'user':user, 'chat': chat, 'beats': beats}
    return render(request, 'base/beat.html', context)

@login_required(login_url='login')
def beatInfo(request, pk):
    search = request.GET.get('search') if request.GET.get('search') else ''
    beats = request.user.beat_set.filter(
        Q(name__icontains=search) |
        Q(creater__username__icontains=search) |
        Q(description__icontains=search)
        )
    if len(beats)==0:
        beats=None
    beat = Beat.objects.get(id=pk)
    if request.method=='POST':
        beat.delete()
        return redirect('home')
    members = beat.members.all()
    context = {'beat': beat, 'beats': beats, 'members': members}
    return render(request, 'base/beat-info.html', context)

@login_required(login_url='login')
def joinBeat(request, pk):
    search = request.GET.get('search') if request.GET.get('search') else ''
    beats = request.user.beat_set.filter(
        Q(name__icontains=search) |
        Q(creater__username__icontains=search) |
        Q(description__icontains=search)
        )
    if len(beats)==0:
        beats=None
    beat = Beat.objects.get(id=pk)
    if request.method == 'POST':
        beat.members.add(request.user)
        mes = Message.objects.create(
            user = request.user,
            beat = beat,
            body = "@"+str(request.user)+" joined beat",
            action = True
        )
        beat.updated = datetime.now()
        beat.save()
        return redirect('beat', pk=beat.id)

    context={'beat': beat, 'beats': beats}
    return render(request, 'base/join-beat.html', context)

@login_required(login_url='login')
def exitBeat(request, pk):
    beat = Beat.objects.get(id=pk)
    if request.user not in beat.members.all():
        return redirect('home')
    if request.method == 'POST':
        beat.members.remove(request.user)
        mes = Message.objects.create(
            user = request.user,
            beat = beat,
            body = "@"+str(request.user)+" exit beat",
            action = True
        )
        # request.user.beat_set.remove(beat)
        return redirect('home')

    context={'beat': beat}
    return render(request, 'base/exit-beat.html', context)

@login_required(login_url='login')
def create(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        creater = request.user
        beat = Beat.objects.create(name=name, creater=creater, description=desc)
        beat.members.add(request.user)
        return redirect('beat', pk=beat.id)
    context = {}
    return render(request, 'base/beat-form.html', context)

@login_required(login_url='login')
def editBeat(request, pk):
    search = request.GET.get('search') if request.GET.get('search') else ''
    beats = request.user.beat_set.filter(
        Q(name__icontains=search) |
        Q(creater__username__icontains=search) |
        Q(description__icontains=search)
        )
    if len(beats)==0:
        beats=None
    beat = Beat.objects.get(id=pk)
    if request.user != beat.creater:
        return redirect('home')
    form = EditBeat(instance=beat)
    if request.method == 'POST':
        form = EditBeat(request.POST, request.FILES, instance=beat)
        print(form)
        if form.is_valid():
            form.save()
            mes = Message.objects.create(
                user = request.user,
                beat = beat,
                body = "@"+str(request.user)+" edit beat",
                action = True
            )
            return redirect('beat-info', pk=beat.id)

    form = EditBeat(instance=beat)
    context = {'beat': beat,'form': form, 'beats': beats}
    return render(request, 'base/edit-beat.html', context)

@login_required(login_url='login')
def deleteMsg(request, pk):
    msg = Message.objects.get(id=pk)
    if request.user != msg.user:
        return redirect('home')
    if request.method == 'POST':
        msg.delete()
        return redirect('beat', pk=msg.beat.id)
    context = {'msg': msg}
    return render(request, 'base/delete-msg.html', context)

@login_required(login_url='login')
def profile(request, un):
    search = request.GET.get('search') if request.GET.get('search') else ''
    beats = request.user.beat_set.filter(
        Q(name__icontains=search) |
        Q(creater__username__icontains=search) |
        Q(description__icontains=search)
        )
    if len(beats)==0:
        beats=None
    user = User.objects.get(username=un)
    form = EditUser(instance=user)
    
    if request.method == 'POST':
        form = EditUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile',user)

        
    context = {'beats': beats, 'user': user, 'form':form}
    return render(request, 'base/profile.html', context)