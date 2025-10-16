
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('authentication.urls')),
    path('api/',include('assessment.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

