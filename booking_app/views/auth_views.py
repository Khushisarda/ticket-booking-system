from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from booking_app.models import User

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')



class LoginView(View):
    def get(self, request):
        # Grab the next parameter so we can redirect after login
        next_url = request.GET.get('next', '')
        return render(request, 'login.html', { 'error': None, 'next': next_url })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST.get('next', '')  # hidden input from form

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to next_url if provided, else to home
            return redirect(next_url or 'home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials',
                'next': next_url
            })

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

