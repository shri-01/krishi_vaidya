from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('options/', views.options, name="options"),
    # Tomato URL's
    path('tomato_analysis/', views.tomato_analysis, name="tomato_analysis"),
    path('tomato/diseases/early_blight', views.early_blight, name='early_blight'),
    path('tomato/diseases/late_bligth', views.late_bligth, name='late_bligth'),
    path('tomato/diseases/Septorial_Disease', views.Septorial_Disease, name='Septorial_Disease'),
    path('tomato/diseases/yellow_curl', views.yellow_curl, name='yellow_curl'),

    # Corn URL's
    path('corn/analysis/', views.corn_analysis, name="corn_analysis"),
    path('corn/diseases/gray_leaf_spot', views.corn_Gray_leaf_spot, name='corn_Gray_leaf_spot'),
    path('corn/diseases/common_rust', views.corn_common_rust, name='corn_common_rust'),
    path('corn/diseases/leaf_blight', views.corn_blight, name='corn_blight'),

    # Bell pepper URL's
    path('bell_pepper/analysis/', views.bellpaper_analysis, name="bellpaper_analysis"),
    path('bell_pepper/diseases/bacterial', views.bellpaper_bact, name='bellpaper_bact'),

    #Potato URL's
    path('potato/analysis/', views.potato_analysis, name="potato_analysis"),
    path('potato/diseases/early_blight', views.potato_early, name='potato_early'),
    path('potato/diseases/late_blight', views.potato_late, name='potato_late'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)