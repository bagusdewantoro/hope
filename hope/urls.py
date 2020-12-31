"""hope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Hope Project" # modify Admin Site Header
admin.site.index_title = "Data & Administration" # modify Admin Index Title

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('artikel/', include('artikel.urls')),
    path('artikel/', include('artikel.urls', namespace='artikel')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# tambahkan gambar
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
