from django.urls import path
from .views import AlbumList, AlbumCreate, AlbumUpdate, AlbumDelete, PhotoList, PhotoCreate, PhotoUpdate, PhotoDelete, PhotoDetail, AlbumWithPhotosList


urlpatterns = [
    path('', AlbumList.as_view()),
    path('create/', AlbumCreate.as_view()),
    path('<int:pk>/', AlbumUpdate.as_view()),
    path('<int:pk>/delete', AlbumDelete.as_view()),
    path('photo/', PhotoList.as_view()),
    path('photo/create/', PhotoCreate.as_view()),
    path('photo/<int:pk>/', PhotoUpdate.as_view()),
    path('photo/<int:pk>/delete', PhotoDelete.as_view()),
    path('photo/detail/<int:pk>/', PhotoDetail.as_view()),
    path('albumwithphotos/', AlbumWithPhotosList.as_view()),
]
