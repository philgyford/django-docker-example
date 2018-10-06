from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path


urlpatterns = [
    path('',
        TemplateView.as_view(template_name='myapp/home.html'),
        name='home'),

    path('admin/', admin.site.urls),
]



if settings.DEBUG:

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
