from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_views(request):
    if request.method == "GET":
      books = Book.objects.all()
      serializer = BookSerializer(books, many=True)
      return Response(serializer.data)
    if request.method == "POST":
      serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET' , 'PUT' , 'DELETE'])
def book_detail_views(request,pk):
  try:
      book = Book.objects.get(pk=pk)
  except Book.DoesNotExist:
      return Response({"error": "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
       serializer = BookSerializer(book)
       return Response(serializer.data)
  if request.method == "PUT":
      serializer = BookSerializer(book, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   
  if request.method == "DELETE":
      book.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def book_add(request)
#     title = request.data.get("title")
#     author = request.data.get("author")
#     price = request.data.get("price")

#     if not title or not author or not price:
#         return Response({"error": "title, author and price are required"})

#     book_obj = Book.objects.crete(title=title, author=author, price=price)
#     print(book_obj)
#     data = book_to_dict(book_obj)

#     data = {
#         "id": book_obj.id,
#         "title" : book_obj.title,
#         "author" : book_obj.author,
#         "price" : book_obj.price,
#     }

#     return Response(data)