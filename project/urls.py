from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from webapp import views
from .settings import base as settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/', views.movieList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
