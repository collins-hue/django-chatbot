from django.urls import include, path 
from chatbot import views 

app_name = 'chatbot'

urlpatterns = [
    path('', views.chatbot_home, name='chatbot_home'),           
 ]