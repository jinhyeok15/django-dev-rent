from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('blog:page-list')
    if request.method == 'POST':
        form = AuthenticationForm(
            request, data=request.POST
        )
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('blog:page-list')
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})
