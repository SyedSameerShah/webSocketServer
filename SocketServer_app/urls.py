from django.urls import path
from .views import simple_message_view

urlpatterns = [
     path('', simple_message_view, name='simple-message-view'),
    
]
