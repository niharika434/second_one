from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def icecreams(request):
    return HttpResponse("<h1><marquee>Which flavour do you want??</h1></marquee>")
def preethi(request):
    return HttpResponse("<h1><marquee>Orange flavoured icecream ...if possible with extra ice</h1></marquee>")