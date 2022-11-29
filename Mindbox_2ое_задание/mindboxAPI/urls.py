from django.contrib import admin
from django.urls import path
from prodcat.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product_list/', ProductAPIView.as_view()),
    path('api/v1/category_list/', CategoryAPIView.as_view()),
    path('api/v1/pair_list/', PairAPIView),
]
