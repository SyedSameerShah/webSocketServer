from django.shortcuts import render


from django.http import HttpResponse

def simple_message_view(request):
    return HttpResponse("Welcome to the chat!")
