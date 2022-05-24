
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from books.models import Book, Order, OrderedBook
from books.serializers import BookSerializer, OrderSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        request = self.request
        queryset = self.queryset
        if request.GET.get('title'):
            queryset = queryset.filter(title__contains=request.GET.get('title'))
        if request.GET.get('author'):
            queryset = queryset.filter(author__contains=request.GET.get('author'))
        if request.GET.get('category'):
            queryset = queryset.filter(category__id=request.GET.get('category'))
        return queryset.all()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.prefetch_related('books').all()
    serializer_class = OrderSerializer


class RecommendedBooks(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):
        ordered_books_categories = OrderedBook.objects.filter(order__user=request.user).values_list('book__category__pk', flat=True)
        queryset = self.get_queryset().filter(category__id__in=ordered_books_categories)    #recommend books according to categories in ordred books

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class DiscountedBooks(generics.ListAPIView):
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):
        ordered_books_categories = OrderedBook.objects.filter(order__user=request.user).values_list('book__category__pk', flat=True)
        queryset = self.get_queryset().filter(category__id__in=ordered_books_categories)    #recommend books according to categories in ordred books

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('books_list', request=request, format=format),
        'orders': reverse('orders_list', request=request, format=format),
        'recommended-books': reverse('recommended_books_list', request=request, format=format)
    })