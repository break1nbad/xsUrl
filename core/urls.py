from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from core import settings, views
from core.views import robots_txt
from django.contrib import admin
from django.conf import settings

# admin.autodiscover()
#
# urlpatterns = patterns('',
#                        url(r'^admin/', include(admin.site.urls)),
#                        url(r'', include('cutter.urls')),
#
#                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#       {'document_root': settings.STATIC_ROOT}),
#                        )

urlpatterns = []

urlpatterns += [
    path("z0n3adm1n5de4/", admin.site.urls),
    path("robots.txt", robots_txt),
    path("", include("home.urls_short")),
]

if settings.DEBUG and not settings.DEBUG_USE_REMOTE_CDN:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
#     # ADD NEW Routes HERE
#     # Leave `Home.Urls` as last the last line
    path("", include("home.urls")),
)
