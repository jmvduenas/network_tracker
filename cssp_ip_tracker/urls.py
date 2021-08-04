"""cssp_ip_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path
from ip_tracker.views import home_view, add_ip_address, delete_ip_address, view_details, update_details, view_network, login_page, logout_user, view_csv
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
        
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('home/', home_view, name = 'home'),
    path('topology/', view_network, name = 'topology'),
    path('add/', add_ip_address, name = 'add'),
    path('view/<int:pk>/', view_details, name = 'view'),
    path('update/<int:pk>/', update_details, name = 'update'),
    path('delete/<int:pk>/', delete_ip_address, name = 'delete'),
    path('view_csv', view_csv, name = 'csv'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)