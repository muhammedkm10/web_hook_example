from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def reciever(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        event = payload.get('event', 'unknown')
        data = payload.get('data', {})
        print('i got the event do something......!')
        print(f"Received event: {event}, Data: {data}")
        return JsonResponse({"message": "i got an event"}, status=200)