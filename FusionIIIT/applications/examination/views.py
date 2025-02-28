from django.db.models.query_utils import Q
from django.http import request,HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponse,redirect
from django.http import HttpResponse, HttpResponseRedirect
import itertools
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from applications.academic_information.models import Student
from applications.globals.models import (DepartmentInfo, Designation,
                                         ExtraInfo, Faculty, HoldsDesignation)


@login_required(login_url='/accounts/login')
def exam(request):
    """
    This function is used to Differenciate acadadmin and all other user.

    @param:
        request - contains metadata about the requested page

    @variables:
        user_details - Gets the information about the logged in user.
        des - Gets the designation about the looged in user.
    """
    user_details = ExtraInfo.objects.get(user = request.user)
    des = HoldsDesignation.objects.all().filter(user = request.user).first()
    if str(des.designation) == "Associate Professor" or str(des.designation) == "Professor" or str(des.designation) == "Assistant Professor" :
        return HttpResponseRedirect('/examination/submit/')
    elif str(request.user) == "acadadmin" :
        return HttpResponseRedirect('/examination/submit/')
    
    return HttpResponseRedirect('/dashboard/')

@login_required(login_url='/accounts/login')
def submit(request):
    return render(request,'../templates/examination/submit.html' , {})

@login_required(login_url='/accounts/login')
def verify(request):
    return render(request,'../templates/examination/verify.html' , {})

@login_required(login_url='/accounts/login')      
def publish(request):
    return render(request,'../templates/examination/publish.html' ,{})


@login_required(login_url='/accounts/login')
def notReady_publish(request):
    return render(request,'../templates/examination/notReady_publish.html',{})