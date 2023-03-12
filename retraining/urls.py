from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from library.views import ReaderViewSet, BooksViewSet, AuthorViewSet


router = routers.SimpleRouter()
router.register('reader', ReaderViewSet)
router.register('books', BooksViewSet)
router.register('author', AuthorViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls
