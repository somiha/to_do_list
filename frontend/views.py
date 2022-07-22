from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.
@login_required(login_url = '/login')
def list(request):
	return render(request, 'frontend/list.html')
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + username)
                print(user)


                return redirect('login')

        context = {'form': form}
    return render(request , 'frontend/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                if request.user.is_staff:
                    return redirect('list')
                return redirect('login')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request , 'frontend/login.html', context)

@login_required(login_url = '/login')
def logoutUser(request):
	logout(request)
	return redirect('login')
