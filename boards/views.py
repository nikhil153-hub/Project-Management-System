from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Board
from .serializers import BoardSerializer


def board_view(request):
    if request.method == 'GET':
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return JsonResponse(serializer.data, status=202, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
