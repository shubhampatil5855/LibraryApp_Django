from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'books', views.BookViewset),
router.register(r'users', views.UserViewset),
router.register(r'student', views.StudentBookViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', ObtainAuthToken.as_view())
]