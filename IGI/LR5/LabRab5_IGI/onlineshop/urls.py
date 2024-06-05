from . import views
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^products/$', views.ProductListView.as_view(), name='products'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
    re_path(r'^manufacturers/$', views.ManufacturerListView.as_view(), name='manufacturers'),
    re_path(r'^manufacturers/(?P<pk>\d+)$', views.ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    re_path(r'^contacts/$', views.Contacts_view, name='contacts'),
    re_path(r'^vacation/$', views.Vacation_view, name='vacation'),
    re_path(r'^reviews/$', views.reviews_list, name='reviews'),
    re_path(r'^privacy_policy/$', views.privacy_policy, name='privacy_policy'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^order_list/$', views.OrderListView.as_view(), name='order_list'),
    re_path(r'^pickup_points/$', views.PickupPointListView.as_view(), name='pickup_points'),
    re_path(r'^orders/$', views.FullOrderListView.as_view(), name='orders'),
    re_path(r'^orders/(?P<order_id>\d+)/edit/$', views.edit_order, name='edit_order'),
    re_path(r'^orders/(?P<order_id>\d+)/delete/$', views.delete_order, name='delete_order'),
    re_path(r'^orders/mark-as-completed/(?P<order_id>\d+)/$', views.mark_as_completed, name='mark_as_completed'),
    re_path(r'^sales/$', views.sales_list, name='sales'),
    re_path(r'^sales_by_hour/$', views.sales_by_hour, name='sales_by_hour'),
    re_path(r'^news/$', views.news_list, name='news_list'),
    re_path(r'^reviews/$', views.review_list, name='review_list'),
    re_path(r'^reviews/add/$', views.add_review, name='add_review'),
    re_path(r'^faq/$', views.faq_list, name='faq_list'),
    re_path(r'^faq/add/$', views.add_faq, name='add_faq'),
    re_path(r'^user_sales/$', views.user_sales, name='user_sales'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^coupons/$', views.coupon_list, name='coupon_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)