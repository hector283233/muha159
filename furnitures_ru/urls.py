from django.urls import path
from .import views

urlpatterns = [
				path('', views.index, name='index'),
				path('products/', views.products, name='products'),
				path('products_agacgapylar/', views.products_agacgapylar, name='products_agacgapylar'),
				path('products_beylekiler/', views.products_beylekiler, name='products_beylekiler'),
				path('products_demirgapylar/', views.products_demirgapylar, name='products_demirgapylar'),
				path('products_demironumler/', views.products_demironumler, name='products_demironumler'),
				path('products_mebeller/', views.products_mebeller, name='products_mebeller'),
				path('about/', views.about, name='about'),
				path('contact/', views.contact, name='contact'),
]