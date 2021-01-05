from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import create_order, order_detail, order_list, delete_order

urlpatterns = [
    path('create', create_order, name='create_order'),
    path('<str:id>/details', order_detail, name='details_order'),
    path('<slug:slug>/delete', delete_order, name='delete_order'),
    path('list_order', order_list, name='list_order'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
