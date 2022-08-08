from django.shortcuts import render
from django.http import HttpRequest,HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import brand,bike_model,bike
from .serializers import brandserializer,bike_modelserializer,bikeserializer

from django.core.files.storage import default_storage

# Create your views here.

def landing(request):
    return HttpResponse('hello')


@csrf_exempt
def brandApi(request,pk=0):
    if request.method=='GET':
        brands=brand.objects.all()
        brands_seri=brandserializer(brands,many=True)
        return JsonResponse(brands_seri.data,safe=False)
    elif request.method=='POST':
        brand_data = JSONParser().parse(request)
        brand_seri = brandserializer(data=brand_data)
        if brand_seri.is_valid():
            brand_seri.save()
            return JsonResponse('Added Successfully...',save=False)
        return JsonResponse('failed to add',save=False)    
    elif request.method=='PUT':
        brand_data = JSONParser().parse(request)
        single_brand= brand.objects.get(brandId=brand_data['brandId'])
        brand_seri = brandserializer(single_brand,data=brand_data)
        if brand_seri.is_valid():
            brand_seri.save()
            return JsonResponse('update successfully',save=False)
        return JsonResponse('failed to update',save=False)
    elif request.method=='DELETE':
        singlebrand = brand.objects.get(brandId=pk)
        singlebrand.delete()
        return JsonResponse('Delete Successfully...',save=False)


@csrf_exempt
def modelApi(request,bk=0,mk=0):
    if request.method=='GET':
        singlebikebrand=brand.objects.get(brandId=bk)
        bmodels = singlebikebrand.bike_model_set.all()
        bikemodel_seri=bike_modelserializer(bmodels,many=True)
        return JsonResponse(bikemodel_seri.data,safe=False)
    elif request.method=='POST':
        bikemodel_data = JSONParser().parse(request)
        bikemodel_seri = bike_modelserializer(data=bikemodel_data)
        if bikemodel_seri.is_valid():
            bikemodel_seri.save()
            return JsonResponse('Added Successfully...',save=False)
        return JsonResponse('failed to add',save=False)    
    elif request.method=='PUT':
        bikemodel_data = JSONParser().parse(request)
        single_bikemodel= bike_model.objects.get(modelId=bikemodel_data['modelId'])
        bikemodel_seri = bike_modelserializer(single_bikemodel,data=bikemodel_data)
        if bikemodel_seri.is_valid():
            bikemodel_seri.save()
            return JsonResponse('update successfully',save=False)
        return JsonResponse('failed to update',save=False)
    elif request.method=='DELETE':
        singlebikemodel = bike_model.objects.get(modelId=mk)
        singlebikemodel.delete()
        return JsonResponse('Delete Successfully...',save=False)


@csrf_exempt
def bikeApi(request,bk=0,mk=0,bbk=0):
    if request.method=='GET':
        singlemodel=bike_model.objects.get(modelId=mk)
        bbike = singlemodel.bike_set.all()
        bike_seri=bikeserializer(bbike,many=True)
        return JsonResponse(bike_seri.data,safe=False)
    elif request.method=='POST':
        bike_data = JSONParser().parse(request)
        bike_seri = bikeserializer(data=bike_data)
        if bike_seri.is_valid():
            bike_seri.save()
            return JsonResponse('Added Successfully...',save=False)
        return JsonResponse('failed to add',save=False)    
    elif request.method=='PUT':
        bike_data = JSONParser().parse(request)
        single_bike= bike.objects.get(bikeId=bike_data['bikeId'])
        bike_seri = bikeserializer(single_bike,data=bike_data)
        if bike_seri.is_valid():
            bike_seri.save()
            return JsonResponse('update successfully',save=False)
        return JsonResponse('failed to update',save=False)
    elif request.method=='DELETE':
        singlebike = bike.objects.get(bikeId=bbk)
        singlebike.delete()
        return JsonResponse('Delete Successfully...',save=False)


@csrf_exempt
def savefile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)