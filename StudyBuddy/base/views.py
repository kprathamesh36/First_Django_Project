from django.shortcuts import render


# Create your views here.

rooms = [    {'id':1,'name':'Learn Python'},
    {'id':2,'name':'Connect with Stars'},
    {'id':3,'name':'Lose Yourself'},
    ]




def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def rooms(request,pk):
    return render(request, 'base/rooms.html')