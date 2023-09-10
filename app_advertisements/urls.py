from django.urls import path
from .views import index, top_sellers, advertisement_post,advertisement_detail
from django.contrib import admin
from .views import regist


urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name="adv-post"),
    path('admin/', admin.site.urls),
    path('registr/',regist,name="registr" ),
    path('advertisement/<int:pk>', advertisement_detail, name="adv-detail")
]
