from django.shortcuts import render
from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    hoods = Neighbourhood.objects.all()
    return render(request, 'profile/profile.html', {"date": date, "profile":profile,"hoods":hoods})

def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm() 
        
    return render(request, 'profile/edit_profile.html', {"date": date, "form":signup_form,"profile":profile})


@login_required(login_url='/accounts/login/')
def hoods(request,id):
    date = dt.date.today()
    post=Neighbourhood.objects.get(id=id)
    brushs = Post.objects.filter(neighbourhood=post)
    business = Business.objects.filter(neighbourhood=post)
    return render(request,'each_hood.html',{"post":post,"date":date,"brushs":brushs, "business":business})

def post_business(request,id):
    date = dt.date.today()
    hood=Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood=hood)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user.profile
            business.neighbourhood = hood
            business.save()
            return redirect('index')
    else:
        form = BusinessForm()
        return render(request,'new_business.html',{"form":form,"business":business,"hood":hood,  "date":date})

def post_new(request,id):
    date = dt.date.today()
    hood=Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(neighbourhood=hood)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.profile = profile
            post.neighbourhood = hood
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request,'new_post.html',{"form":form,"posts":posts,"hood":hood,  "date":date})

def post_business(request,id):
    date = dt.date.today()
    hood=Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood=hood)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user.profile
            business.neighbourhood = hood
            business.save()
            return redirect('index')
    else:
        form = BusinessForm()
        return render(request,'new_business.html',{"form":form,"business":business,"hood":hood,  "date":date})
