from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

WEBHOOK_URL = "http://127.0.0.1:8001/webhook_reciever"

# Create your views here.
def send_event(request):
    if request.method == "POST":
        first_number = int(request.POST.get('first_number'))
        second_number = int(request.POST.get('second_number'))
        operation = request.POST.get('operation')
        if not operation:
            return JsonResponse({"error":"select the operation type"})
        result = first_number + second_number if operation == "addition" else first_number - second_number
        payload = {
            "event":f'{operation} event happend in the first app',
            "data":f"The answer is {result}"
        }
        response = requests.post(
             WEBHOOK_URL,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        print("the response is ",response)
        return JsonResponse({"message":f"operation done answer is {result}"})
    return render(request,'home.html')