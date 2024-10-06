"""
URL configuration for TRT_watersystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from TRT_watersystem import settings, views 
import logging

db_logger = logging.getLogger('db')

handler404 = 'TRT_watersystem.views.error_404'
handler500 = 'TRT_watersystem.views.error_500'

try: 
    urlpatterns = [
        path('admin/', admin.site.urls),
        re_path(r"^$", views.index, name="Home Page"),
    ] 
except Exception as e:
    db_logger.exception(e)

# added per A2 hosting Django instructions
# https://www.a2hosting.com/kb/developer-corner/python/installing-and-configuring-django-on-linux-shared-hosting
if hasattr(settings, 'STATIC_ROOT'):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# specify image upload url for the development mode
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
