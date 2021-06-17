from django.urls import path
from stnk import views


urlpatterns = [
    path('home', views.home),
    path('opd/',views.TambahOpd.as_view(), name='tambah-opd'),
    path('list_stnk/', views.LihatAsset.as_view(), name='listdata'),
    path('tambah_data/',views.TambahAsset.as_view(), name='tambah-data'),
    path('edit/<int:id>/',views.EditAsset.as_view(),name='editdata'),
    path('hapus/<int:id>/',views.HapusAsset.as_view(),name='hapus'),
    path('update/<int:id>', views.UpdateData.as_view(), name='update-data'),

]