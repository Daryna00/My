from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import create_order, order_detail, order_list

urlpatterns = [
    path('create', create_order, name='create_order'),
    path('<slug:slug>/details', order_detail, name='order_detail'),
    path('list', order_list, name='order_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
