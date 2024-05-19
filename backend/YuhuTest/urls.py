from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Yuhu Test - Tasks Manager",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def main(request):
    return render(request, "index.html")

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', main, name='home'),
    path('', include('tasks.urls')), 
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]
