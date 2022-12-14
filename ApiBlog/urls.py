"""ApiBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls





schema_view = get_swagger_view(title='Post API')

# app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('docs/',get_swagger_view(title='Posts API')),
    path('api/docs', include_docs_urls(title='Posts API')),
    # path('api/', include(router.urls))
    
]

#to serve images anf other static files we use this settings ...
#we first import static and settings as shown in lines 18/19
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)