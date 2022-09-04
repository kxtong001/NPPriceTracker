from django.urls import path
from .views import ItemListView, ItemDeleteView , ItemDetailView ,  update_prices

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('delete/<pk>/', ItemDeleteView.as_view(), name="delete"),
    path('item/<int:pk>/', ItemDetailView.as_view(), name="itemdetail"),
    path('update/',  update_prices, name='update-prices'),
]
