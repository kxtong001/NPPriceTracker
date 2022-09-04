from django.urls import path
from landing.views import Index, HowTo, About

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('howto/', HowTo.as_view(), name='HowTo'),
    path('about/', About.as_view(), name='About'),
    
]