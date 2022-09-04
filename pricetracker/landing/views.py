from django.shortcuts import render
from django.views import View
# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

class HowTo(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/howto.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/about.html')