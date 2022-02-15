import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, \
    SpectacularSwaggerView

from common.urls import router as common_router
from common.views import CustomTokenObtainPairView, \
    CustomTokenRefreshView
from persons.urls import router as persons_router
from posts.urls import router as posts_router

admin.site.site_header = 'Social Media Lists'
admin.site.index_title = 'Social Media Lists'
admin.site.enable_nav_sidebar = False

urlpatterns = [
    # authentication
    path(
        'api/auth/token/', 
        CustomTokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/auth/token/refresh/', 
        CustomTokenRefreshView.as_view(), name='token_refresh'
    ),

    path('admin/', admin.site.urls),
    path('api/', include(common_router.urls)),
    path('api/', include(persons_router.urls)),
    path('api/', include(posts_router.urls)),

    # documentation
    path(
        'api/schema/', 
        SpectacularAPIView.as_view(), name='schema'
    ),
    path(
        'api/docs/', 
        SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'
    )
]

if settings.DEBUG:
    # media files
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    
    if settings.ENABLE_DEBUG_TOOLBAR:
        # django-debug-toolbar
        urlpatterns.append(
            path('__debug__/', include(debug_toolbar.urls))
        )
