from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from book import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
  url(r'^', include(router.urls))
]

