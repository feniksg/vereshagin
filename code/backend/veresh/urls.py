from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from veresh.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.urls import path, include

def redirect_to_frontend(request):
    return HttpResponseRedirect('http://localhost:3000')

schema_view = get_schema_view(
    openapi.Info(
        title="Veresh",
        default_version='v1',
        description="...",
        terms_of_service="https://google.com",
        contact=openapi.Contact(email="admin@mail.ru"),
        license=openapi.License(name="open"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

start_url = 'api/'
urlpatterns = [
    path('', redirect_to_frontend),
    path(start_url+"admin/", admin.site.urls),
    path(start_url+'v1/', include("api.urls"))
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
if DEBUG:
    urlpatterns += [
        
        path(start_url+'api-info/', 
             schema_view.with_ui('swagger', cache_timeout=0), 
             name='schema-swagger-ui'),
        path(start_url+'api-info/redoc/', 
             schema_view.with_ui('redoc', cache_timeout=0), 
             name='schema-redoc'),
    ]