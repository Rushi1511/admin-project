from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def leads_view(request):
    return render(request, 'dashboard/leads.html')

