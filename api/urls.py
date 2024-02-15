from django.urls import path
from .views.category_view import CategoryDetail, CategoryList, CategoryCreate
from .views.retailer_view import RetailerDetail, RetailerList, RetailerCreate
from .views.vendor_view import VendorList, VendorCreate, VendorDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('category/', CategoryCreate.as_view()),
    path('category/<int:id>', CategoryDetail.as_view()),
    path('retailers/', RetailerList.as_view()),
    path('retailer/', RetailerCreate.as_view()),
    path('retailer/<int:id>', RetailerDetail.as_view()),
    path('vendors/', VendorList.as_view()),
    path('vendor/', VendorCreate.as_view()),
    path('vendor/<int:id>', VendorDetail.as_view()),
]   
