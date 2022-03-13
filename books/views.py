
from rest_framework import generics, permissions
from rest_framework.response import Response
from books.models import Book, Order, OrderedBook
from books.serializers import BookSerializer, OrderSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()

        if request.GET.get('title'):
            queryset = queryset.filter(title__contains=request.GET.get('title'))
        if request.GET.get('author'):
            queryset = queryset.filter(author__contains=request.GET.get('author'))
        if request.GET.get('category'):
            queryset = queryset.filter(category__id=request.GET.get('category'))

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.prefetch_related('books').all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class RecommendedBooks(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):
        ordered_books_categories = OrderedBook.objects.filter(order__user=request.user).values_list('book__category__pk', flat=True)
        queryset = self.get_queryset().filter(category__id__in=ordered_books_categories)    #recommend books according to categories in ordred books

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)