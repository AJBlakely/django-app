from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_index, name='book-index'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('books/<int:book_id>/add-status/', views.add_status, name='add-status'),
    path('genres/', views.GenreList.as_view(), name='genre-index'),
    path('genres/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete'),
    path('books/<int:book_id>/associate-genre/<int:genre_id>/', views.associate_genre, name='associate-genre'),
    path('books/<int:book_id>/remove-genre/<int:genre_id>/', views.remove_genre, name='remove-genre'),
]
