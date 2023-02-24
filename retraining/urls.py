from django.contrib import admin
from django.urls import path
from rest_framework import routers

from library.views import ReaderViewSet, BooksViewSet, AuthorViewSet

router = routers.SimpleRouter()
router.register('reader', ReaderViewSet)
router.register('books', BooksViewSet)
router.register('author', AuthorViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
