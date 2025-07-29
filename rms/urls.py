from django.urls import path,include
from .views import*
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',CategoryViewset, basename = 'categories')
router.register(r'Foods', Foodviewset, basename = 'foods')

urlpatterns = [
    # path('categories/', CategoryViewset.as_view({'get':'list', 'post':'create'})),
    # path('categories/<pk>/', CategoryViewset.as_view({'get':'retrive', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}))
    # path('categories/', CategoryView.as_view()),
    # path('categories/<pk>/', CategoryDetail.as_view()), 
    # path('category/', category_list),
    # path('category/<id>/', category_details)
] + router.urls
