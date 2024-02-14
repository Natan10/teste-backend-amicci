from django.urls import path
from .views.category_view import CategoryDetail, CategoryList

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('category/<int:id>', CategoryDetail.as_view()),
]
