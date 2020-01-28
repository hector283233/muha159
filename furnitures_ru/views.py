from django.shortcuts import render
from django.http import HttpResponse


from .models import Group_ru, Product_ru, Main_Page_ru

def index(request):
	productsBK = Product_ru.objects.filter(product_group__group_type='BK').order_by('-pk')[:1]
	productsDG = Product_ru.objects.filter(product_group__group_type='DG').order_by('-pk')[:1]
	productsAG = Product_ru.objects.filter(product_group__group_type='AG').order_by('-pk')[:1]
	productsMB = Product_ru.objects.filter(product_group__group_type='MB').order_by('-pk')[:1]
	productsDO = Product_ru.objects.filter(product_group__group_type='DO').order_by('-pk')[:1]
	page_content = Main_Page_ru.objects.all
	
	context = {'page_content': page_content, 
			   'productsBK': productsBK, 
			   'productsDG': productsDG,
			   'productsAG': productsAG,
			   'productsMB': productsMB,
			   'productsDO': productsDO}
	return render(request, "furnitures_ru/index.html", context)

def products(request):
	productsBK = Product_ru.objects.filter(product_group__group_type='BK').order_by('-pk')
	productsDG = Product_ru.objects.filter(product_group__group_type='DG').order_by('-pk')
	productsAG = Product_ru.objects.filter(product_group__group_type='AG').order_by('-pk')
	productsMB = Product_ru.objects.filter(product_group__group_type='MB').order_by('-pk')
	productsDO = Product_ru.objects.filter(product_group__group_type='DO').order_by('-pk')
	groupsBK = Group_ru.objects.filter(group_type = 'BK')
	groupsDG = Group_ru.objects.filter(group_type = 'DG')
	groupsAG = Group_ru.objects.filter(group_type = 'AG')
	groupsMB = Group_ru.objects.filter(group_type = 'MB')
	groupsDO = Group_ru.objects.filter(group_type = 'DO')
	
	context = {
			   'productsBK': productsBK, 
			   'productsDG': productsDG,
			   'productsAG': productsAG,
			   'productsMB': productsMB,
			   'productsDO': productsDO,
			   'groupsBK':groupsBK,
			   'groupsDG':groupsDG,
			   'groupsAG':groupsAG,
			   'groupsMB':groupsMB,
			   'groupsDO':groupsDO,
			   }
	return render(request, 'furnitures_ru/products.html', context)

def products_agacgapylar(request):
	groups = Group_ru.objects.filter(group_type = 'AG')
	productsAG = Product_ru.objects.filter(product_group__group_type='AG').order_by('product_group').order_by('-pk')
	context = {'productsAG':productsAG, 'groups':groups}
	return render(request, 'furnitures_ru/products_agacgapylar.html', context)

def products_beylekiler(request):
	groups = Group_ru.objects.filter(group_type = 'BK')
	productsBK = Product_ru.objects.filter(product_group__group_type='BK').order_by('product_group').order_by('-pk')
	context = {'productsBK':productsBK, 'groups':groups}
	return render(request, 'furnitures_ru/products_beylekiler.html', context)

def products_demirgapylar(request):
	groups = Group_ru.objects.filter(group_type = 'DG')
	productsDG = Product_ru.objects.filter(product_group__group_type='DG').order_by('product_group').order_by('-pk')
	context = {'productsDG':productsDG, 'groups':groups}
	return render(request, 'furnitures_ru/products_demirgapylar.html', context)

def products_demironumler(request):
	groups = Group_ru.objects.filter(group_type = 'DO')
	productsDO = Product_ru.objects.filter(product_group__group_type='DO').order_by('product_group').order_by('-pk')
	context = {'productsDO':productsDO, 'groups':groups}
	return render(request, 'furnitures_ru/products_demironumler.html', context)

def products_mebeller(request):
	groups = Group_ru.objects.filter(group_type = 'MB')
	productsMB = Product_ru.objects.filter(product_group__group_type='MB').order_by('product_group').order_by('-pk')
	context = {'productsMB':productsMB, 'groups':groups}
	return render(request, 'furnitures_ru/products_mebeller.html', context)

def about(request):
	return render(request, 'furnitures_ru/about.html')

def contact(request):
	return render(request, 'furnitures_ru/contact.html')