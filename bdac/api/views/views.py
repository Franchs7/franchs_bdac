from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
def Login(request):
    res = {'a':1,'b':2}
    return JsonResponse(res)