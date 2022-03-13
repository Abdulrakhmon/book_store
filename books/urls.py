from django.urls import path
from .views import BookList, OrderList, RecommendedBooks

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view()),
    path('books/', BookList.as_view()),
    path('orders/', OrderList.as_view()),
    path('recommended-books/', RecommendedBooks.as_view()),
]