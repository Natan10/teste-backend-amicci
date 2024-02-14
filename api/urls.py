from django.urls import path
from .views.category_view import CategoryDetail, CategoryList, CategoryCreate
from .views.retailer_view import RetailerDetail, RetailerList, RetailerCreate

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('category/', CategoryCreate.as_view()),
    path('category/<int:id>', CategoryDetail.as_view()),
    path('retailers/', RetailerList.as_view()),
    path('retailer/', RetailerCreate.as_view()),
    path('retailer/<int:id>', RetailerDetail.as_view()),
]   
