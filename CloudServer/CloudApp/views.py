from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def Hi(request):
    return render(request, 'CloudApp/Index.html')
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')

    return render(request,'accounts/login.html')
def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account Created for " + user + " Succesfully" )

            return redirect('login')


    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def Admin(request):
    pass



