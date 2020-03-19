from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books_info_app.models import Book
from books_info_app.serializers import BookSerializer

class booklist(APIView):
    
    def get(self, request):
        #retrieve all books from DB
        allbooks = Book.objects.all()

        #serialized all books - turn into JSON
        #many = true means there are many of them so you don’t have return just one JSON object.
        serializer = BookSerializer(allbooks,many=True)

        #return the response with seralized books in JSON format
        return Response(serializer.data)

    def post(self,request):
        pass