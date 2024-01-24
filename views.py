
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

valid_licenses={"license_key1":{"status": "active"}, "license_key2": {"status": "inactive"}}

@csrf_exempt
@require_POST
def validate_license(request):
    data=json.load(request.body.decode('utf_8'))
    license_key=data.get('license_key')

    if license_key in valid_licenses:
        return JsonResponse({"status":valid_licenses[license_key]["status"]})
    else:
        return JsonResponse({"status": "invalid"})

@csrf_exempt
@require_POST
def activate_license(request):
    data=json.loads(request.body.decode('utf-8'))
    license_key=data.get('license_key')

    valid_licenses[license_key]={"status": "active"}
    return JsonResponse({"status": "activated"})

def usage_statistics(request):
    statistics={"active_license": len(valid_licenses), "usage_patterns":{}}
    return JsonResponse(statistics)

# Create your views here.
