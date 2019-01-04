from rest_framework import viewsets
from book.models import Book
from book.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides list, create, retrieve,
  update, destroy actions.
  """
  queryset = Book.objects.all()
  serializer_class = BookSerializer

