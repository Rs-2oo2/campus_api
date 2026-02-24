from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assignments.views import AssignmentViewSet
from accounts.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet, basename='assignments')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('api/', include(router.urls)),
]