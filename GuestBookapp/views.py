from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# from .models import User, Email
# Create your views here.


def index(request):

    # Authenticated users view their inbox
    # if request.user.is_authenticated:
        return render(request, "GuestBookapp/index.html")

    # Everyone else is prompted to sign in
    # else:
    #     return HttpResponseRedirect(reverse("login"))
