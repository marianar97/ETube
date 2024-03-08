from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'socialnetwork/home.html', {'range': range(18) })

def login(request):
    return render(request, 'socialnetwork/login.html')

