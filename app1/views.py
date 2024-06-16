from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def main(request):

    return HttpResponse('\n'.join(list(Product.objects.all())))