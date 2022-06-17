from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('analysis/', views.analysis, name="analysis"),
    path('diseases/early_blight', views.early_blight, name='early_blight'),
    path('diseases/late_bligth', views.late_bligth, name='late_bligth'),
    path('diseases/Septorial_Disease', views.Septorial_Disease, name='Septorial_Disease'),
    path('diseases/yellow_curl', views.yellow_curl, name='yellow_curl'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)