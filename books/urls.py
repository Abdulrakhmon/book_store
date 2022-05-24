from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BookList, OrderList, RecommendedBooks, api_root, BookDetail

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view()),
    path('', api_root),
    path('books/', BookList.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('orders/', OrderList.as_view(), name='orders_list'),
    path('recommended-books/', RecommendedBooks.as_view(), name='recommended_books_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)