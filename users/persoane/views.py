from django.shortcuts import render
from .models import User
# Create your views here.

def user_list(request):
    users=User.objects.all()
    context={'user':users}
    return render(request,'list.html',context)