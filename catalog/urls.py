
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.BookListView.as_view(),name = 'books'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name = 'book-detail')

]
