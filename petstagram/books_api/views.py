from django.shortcuts import get_object_or_404
from rest_framework import views, response, status
from petstagram.books_api.models import Book
from petstagram.books_api.serializers import BookSerializer


def get_book_object(pk):
    return get_object_or_404(Book, pk=pk)


class ListBooksView(views.APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return response.Response({"books": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBookSetView(views.APIView):
    def get(self, pk):
        book = get_book_object(pk)
        serializer = BookSerializer(book)
        return response.Response({"book": serializer.data})

    def put(self, request, pk):
        book = get_book_object(pk)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = get_book_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_book_object(pk)
        book.delete()
        return response.Response(status=status.HTTP_200_OK)

