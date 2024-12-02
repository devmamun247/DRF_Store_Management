from django.shortcuts import render
# from django.shortcuts import render, HttpResponse
from .models import Model
from .serializer import ModelSerializer
from rest_framework import viewsets
from rest_framework.response import Response 


#django replace with DRF
# class ModelViewSet(viewsets.ModelViewSet):
class ModelViewSet(viewsets.GenericViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    def list(req, self):
        queryset = Model.objects.all()
        serializer = ModelSerializer(queryset,many=True)
        print(serializer)
        return Response(serializer.data)




# ======================================================
# Create your views here.

# def index (req):

#     return render(req, 'index.html')


# def index2 (req):

#     return HttpResponse(req)

#======================================================
# def index (req):
#     models = Model.objects.all()
#     print(models)

#     return HttpResponse(req)

# (above & below both are same)

# this is django 
# def index (req):
#     models = Model.objects.get(id=1)
#     print(models.name)

#     return HttpResponse(req)
#======================================================
#django replace with DRF

