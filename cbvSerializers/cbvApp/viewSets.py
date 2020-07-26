from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class StudentPagination(PageNumberPagination):
    page_size=1
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=LimitOffsetPagination