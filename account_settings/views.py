from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import hashers

def account(request):
    if request.session['member_id'] == 0:
        return redirect('/')
    return render(request, 'account_settings/account_page.html')

def saving_account(request):
    user_id = request.session['member_id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']

    user = User.objects.get(id=user_id)
    user.username=username
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.save()

    messages.info(request, "Settings changed successfully !")
    return redirect('account_settings:account')

def change_password(request):

    if request.method == "POST":
        user_id = request.session['member_id']
        oldpass = request.POST['old_pass']
        newpass = request.POST['new_pass']
        conpass = request.POST['con_pass']

        user = User.objects.get(id=user_id)

        my_pass = hashers.check_password(oldpass, user.password)

        if my_pass:
            if newpass == conpass:
                user.set_password(conpass)
                user.save()
                messages.info(request, "Passowrd changed success...login to verify !")
                return redirect('/')
            else:
                messages.info(request, "New passwords do not match")
                return redirect('account_settings:change_password')
        else:
            messages.info(request, "Invalid old password")
            return redirect('account_settings:change_password')

    else:
        if request.session['member_id'] == 0:
            return redirect('/')
        else:
            return render(request, 'account_settings/change_pass.html')