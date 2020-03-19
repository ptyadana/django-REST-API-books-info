from rest_framework import serializers
from books_info_app.models import Book

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        #same as 
        # fields = '__all__'
        fields = [id,book_name,author_name,book_price,book_quantity]