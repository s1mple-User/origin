
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('118n', include('django.conf.urls.i18n')),

]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('', include("blogging.urls")),
    path('', include("report.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
