from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def login_view(request):
    data = json.loads(request.data)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse({"details":"please provide username and password"})
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"details":"invalid credentials"}, status=400)
    login(request, user)
    return JsonResponse({"details":"successfully login"})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"details": "there are not logged in!"}, status=400)
    logout(request)
    return JsonResponse({"details": "successfully logged out"})

@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"is_authenticated": False})
    return JsonResponse({"is_authenticated": True})

def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"is_authenticated": False})
    return JsonResponse({"username": request.user.username})
