from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoViewset,Auth

router = DefaultRouter()
router.register("todo",TodoViewset)
router.register("auth",Auth,basename="auth")

urlpatterns = [
    path("api/",include(router.urls))
]