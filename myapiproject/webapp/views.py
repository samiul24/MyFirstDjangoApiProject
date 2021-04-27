from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from . models import employees
from . serializers import employeesSerializer
from rest_framework import generics
from rest_framework import mixins

class employeeList(APIView):
    def get(self, request):
        employee1=employees.objects.all()
        serializer=employeesSerializer(employee1, many=True)
        return Response(serializer.data)


class genericApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = employeesSerializer
    queryset = employees.objects.all()

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)


@csrf_exempt
def employeeaddget(request):
    if request.method=='GET':
        employee1=employees.objects.all()
        serializer=employeesSerializer(employee1, many=True)
        return JsonResponse(serializer.data,  safe=False)

    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = employeesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@api_view(['GET','POST'])
def employeeadd_get(request):
    if request.method=='GET':
        employee1=employees.objects.all()
        serializer=employeesSerializer(employee1, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = employeesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def employeedetails(request,pk):
    try:
        employee1=employees.objects.get(pk=pk)
    except employees.DoesNotExist:
        return HttpResponse(status=400)

    if request.method=="GET":
        serializer = employeesSerializer(employee1)
        return JsonResponse(serializer.data)

    elif request.method=="DELETE":
        employee1.delete()

    elif request.method=="PUT":
        data = JSONParser().parse(request)
        serializer=employeesSerializer(employee1, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.error, status=400)
