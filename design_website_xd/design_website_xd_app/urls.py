from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout_view, name='logout'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('service/<int:id>/', views.service_template, name='service'),
    path('account/', views.account, name='account'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)