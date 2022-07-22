from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.urls.conf import re_path
from django.views.static import serve

from project.settings import DEBUG

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # INCLUDE APPS
    path('', include('home.urls')),
    path('', include('deezer.urls'))
]

# INCLUDE STATIC
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# INCLUDE MEDIA
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if DEBUG:
    import debug_toolbar 
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
