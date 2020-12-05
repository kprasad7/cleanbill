from django.urls import path, include
from tech import views

urlpatterns = [
    path('tech',views.myapp , name='myapp'),
    path('numm' , views.tandu,name='tandu'),
    path('contact' , views.app,name='app'),
    path('price' , views.price,name='price'),
    
    
]