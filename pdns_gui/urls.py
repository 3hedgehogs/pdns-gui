from django.conf import settings
from django.urls import include, path

from django.contrib import admin

admin.autodiscover()

urlpatterns = [path("jet/", include("jet.urls", "jet")), path("", admin.site.urls)]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
