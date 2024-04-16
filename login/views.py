from django.shortcuts import render

def registerHandler(request):
    return render(request, 'cadastro.html')

def loginHandler(request):
    return render(request, 'login.html')
