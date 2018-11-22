from django.shortcuts import render,redirect
from beerapp.models import BeerBar
from beerapp.forms import BeerBarForm,UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def show(request):
    return render(request,'beerapp/home.html')
@login_required()
def beerlist(request):
    beer = BeerBar.objects.all()
    return render(request,'beerapp/beer_list.html',{'beer':beer})
@login_required()
def addbeer(request):
    form = BeerBarForm()
    if request.method =='POST':
        form = BeerBarForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return  redirect('/')
    return render(request,'beerapp/add_beer.html',{'form':form})

def beerupdate(request,id):
    beer=BeerBar.objects.get(id=id)
    if request.method=='POST':
        form=BeerBarForm(request.POST,instance=beer)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'beerapp/update.html',{'beer':beer})
def action(request):
    return render(request,'beerapp/action.html')
def deletebeer(request,id):
    beer = BeerBar.objects.get(id=id)
    beer.delete()
    return redirect('/')
def Signup(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            last_name = form.cleaned_data['last_name']
            password= form.cleaned_data['password']
            User.objects.create_user(username  = username ,first_name = first_name,email=email,last_name = last_name,password = password)
            messages.success(request,'user registeration successfuly')
            return redirect('/signup')
    else:
        form = UserForm
    return render(request,'beerapp/signup.html',{'form':form})
def Login(request):
    if request.method=='POST':
        username = request.POST['user']
        password = request.POST['pas']
        try:
            User = auth.authenticate(username=username,password=password)
            if User is not None:
                 auth.login(request,User)
                 return render(request,'beerapp/home.html')
            else:
                messages.error(request,'username and password does not exit')
        except ObjectDoesNotExist:
            print('invalid user')
    return render(request,'beerapp/login.html')
def     Logout(request):
    auth.logout(request)
    return  render(request,'beerapp/login.html')
def search(request):
    if request.method == 'POST':
            srch = request.POST['srh']
            if srch:
                match = BeerBar.objects.filter(Q(bname__icontains=srch))
                if match:
                    return render(request, 'beerapp/search.html', {'sr': match})
                else:
                    messages.error(request, 'no result found')
            else:
                return redirect('/search')


    return render(request,'beerapp/search.html')




