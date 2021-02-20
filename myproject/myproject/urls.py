from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path


urlpatterns = [
    path('',
        TemplateView.as_view(template_name='myapp/home.html'),
        name='home'),

    path('admin/', admin.site.urls),
]
