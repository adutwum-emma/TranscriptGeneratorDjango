from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SchoolLogo
from django.contrib.auth.models import auth, User
from django.contrib import messages



def index(request):

    school_logo = SchoolLogo.objects.get(file_name='UEW')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['member_id'] = user.id
            return redirect('dash_board:main_panel')
        else:
            messages.info(request, "Invalid Login")
            return redirect("/")
        
    else:
        return render(request, "home/login_page.html", {'my_logo':school_logo})
        

def logout(request):
    
    auth.logout(request)
    request.session['member_id'] = 0
    return redirect('/')