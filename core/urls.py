from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('courses/', include('courses.urls', namespace='courses')),
    path('payment/', include('payment.urls', namespace='payment')),


    path('', HomeView.as_view(), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)