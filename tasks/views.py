from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Task


@csrf_exempt
def add_new_task(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        post_data = {
            "name": json_data.get("name"),
            "description": json_data.get("description"),
            "email": json_data.get("email"),
        }
        try:
            Task.objects.create(**post_data)
            return HttpResponse("New task created!", status=200)
        except Exception as e:
            return HttpResponse("Something went wrong", status=500)
    else:
        return HttpResponse("Method not allowed", status=405)


def get_all_task(request):
    if request.method == "GET":
        data = {"data": []}
        for obj in Task.objects.all():
            data["data"].append(
                {
                    "id": obj.id,
                    "name": obj.name,
                    "description": obj.description,
                    "email": obj.email,
                    "createdAt": obj.createdAt,
                }
            )
        return JsonResponse(data)
    else:
        return HttpResponse("Method not allowed", status=500)
