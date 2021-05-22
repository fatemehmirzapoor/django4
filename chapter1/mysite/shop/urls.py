from django.urls import path
from .views import shop_list, shop_detail
app_name = 'shop'
urlpatterns = [
 # post views
    path('',shop_list, name='shop_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
      shop_detail,
      name='post_detail'),
    ]