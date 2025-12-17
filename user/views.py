from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect()
        
#     else:
#         form = RegisterForm()

#     context = {
#         'form':form,
#     }
#     return render(request, 'user/register.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'user/login.html', {'error':'Invalid credentials'})
        
        user = authenticate(request, username=user_obj, password=password)

        if user is not None:
            login(request, user)
            return redirect('my_portfolio:index')
        else:
            context = {
                'error': 'Invalid Credentials'
            }
            return render(request, 'user/login.html', context)
        
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return redirect('my_portfolio:index')




