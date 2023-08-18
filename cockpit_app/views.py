from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    #return HttpResponse('Welcome to Django')
    return render(request, 'index.html', {})

def login(request):
    if request.method == "POST":
        global auth_code
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_code = request.POST.get('auth-code')
        if username == "bigtrader" and password == "bigtrader@123" and auth_code != None:
            return render(request, 'go.html', { 'auth_code': auth_code})
        else:
            return render(request, 'index.html')
        
def trade(request):
    param = request.GET.get('value')
    token = request.GET.get('auth-token')

    url = "https://api.tradetron.tech/api"
    params = {
        #615be258-009f-4b97-b4bb-a97603469aa5
        "auth-token": token,
        "key": "nifty50",
        "value": param
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return HttpResponse(response.text)
    else:
        return HttpResponse("Algo Error - Tradetron server down")
