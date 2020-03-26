from django.shortcuts import render, redirect
from django.views.generic import View

# Importar metodo de auntenticacion
from django.contrib.auth import authenticate
# Create your views here.
def index (request):
    return render(request,'index.html')

def landing (request):
    return render(request,'landing.html')

class LoginClass(View):
    templates = 'Login/index.html'
    templates_ok = 'Landing/landing.html'
    templates_oke = 'Dashboard/dashboard.html'
    def get(self, request, *args, **kwargs):
        print("GET")
        return render(request, self.templates,{})

    def post(self, request, *args, **kwargs):
        print("POST")
        user_post = request.POST['user']
        password_post = request.POST['password']

        user_session = authenticate(username = user_post, password=password_post)

        if user_session is not None:
            return redirect ('Login:dashboard')
            # return render(request, self.templates_oke,{})
        else:
            self.message = 'Usuario o contraseña incorrecta'
            return render(request, self.templates, self.get_context())

    def get_context(self):
        return{
            'error':self.message,
        }

class LandingClass(View):
    templates_ok = 'Landing/landing.html'
    def get(self, request, *args, **kwargs):
        print("GET")
        return render(request, self.templates_ok,{})

class DashboardClass(View):
    templates_oke = 'Dashboard/dashboard.html'
    def get(self, request, *args, **kwargs):
        print("GET")
        return render(request, self.templates_oke,{})