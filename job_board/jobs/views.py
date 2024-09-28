from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jobs.serializer import Industyserializers,Companyserializers,JobPostserializers,Reviewserializers,Applicationserializers
from jobs.models import Company,Application,JobPost,Industries,Review
from rest_framework.decorators import api_view

@api_view(['GET','POST'])

def get_industries(request):

    if request.method == 'GET':

        obj = Industries.objects.first()
        ser = Industyserializers(obj, many = True).data
        return JsonResponse(ser, safe = False)
    
    if request.method == 'POST':

        data = request.data
        obj = Industyserializers(data = data, many = True)
        if obj.is_valid(raise_exception=True):
            obj.save()
            return JsonResponse(obj.data, safe = False)
        else:
            return JsonResponse(obj.errors, safe = False)






