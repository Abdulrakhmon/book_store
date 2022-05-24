from rest_framework import serializers

from books.models import Book, Order, OrderedBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'category', 'image', 'description', 'author', 'published_date', 'price')
        model = Book
        depth = 1


class OrderedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedBook
        fields = ['book', 'quantity', 'price']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book_detail', read_only=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        fields = ('id', 'number', 'total_quantity_of_items', 'total_amount_of_purchase', 'status', 'created_at', 'books')
        model = Order
        depth = 1