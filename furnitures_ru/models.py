from django.db import models

class Group_ru(models.Model):
	TYPES = (
				('DG', 'Demir Gapylar'),
				('AG', 'Agaç Gapylar'),
				('MB', 'Mebeller'),
				('DO', 'Demir Önümler'),
				('BK', 'Beýlekiler'),
			)
	group_name			= models.CharField("Имя группы", max_length=128)
	group_type			= models.CharField("Тип группы", max_length=2, choices=TYPES)

	def __str__(self):
		return self.group_name
			

class Product_ru(models.Model):
	product_name		= models.CharField("Имя продукта", max_length=128)
	product_group		= models.ForeignKey(Group_ru, on_delete=models.SET_NULL, null=True, verbose_name="Группа")
	product_image 		= models.ImageField("Фото", upload_to = 'images/', default = 'images/default.jpg')
	product_description = models.TextField("Подробно")
	is_new				= models.BooleanField("Новый", default=0)

	def __str__(self):
		return self.product_name

class Main_Page_ru(models.Model):
	img_slide1 			= models.ImageField("Слайд1", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide2 			= models.ImageField("Слайд2", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide3 			= models.ImageField("Слайд3", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide4 			= models.ImageField("Слайд4", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide5 			= models.ImageField("Слайд5", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide6 			= models.ImageField("Слайд6", upload_to = 'furnitures/images/', default = 'default.jpg')

	text_slide1 		= models.CharField("Слайд1 текст", max_length=32)
	text_slide2 		= models.CharField("Слайд2 текст", max_length=32)
	text_slide3 		= models.CharField("Слайд3 текст", max_length=32)
	text_slide4 		= models.CharField("Слайд4 текст", max_length=32)
	text_slide5 		= models.CharField("Слайд5 текст", max_length=32)
	text_slide6 		= models.CharField("Слайд6 текст", max_length=32)

	description_slide1 	= models.TextField("Слайд1 Подробно")
	description_slide2 	= models.TextField("Слайд2 Подробно")
	description_slide3 	= models.TextField("Слайд3 Подробно")
	description_slide4 	= models.TextField("Слайд4 Подробно")
	description_slide5 	= models.TextField("Слайд5 Подробно")
	description_slide6 	= models.TextField("Слайд6 Подробно")

	company_name 		= models.CharField(max_length=64)

	about_company		= models.TextField('Kärhana Barada Giňişleýin')

	property1			= models.ImageField("Icon1", upload_to = 'furnitures/images/', default = 'default.jpg')
	property2			= models.ImageField("Icon2", upload_to = 'furnitures/images/', default = 'default.jpg')
	property3			= models.ImageField("Icon3", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property1		= models.TextField("Услуга1")
	text_property2		= models.TextField("Услуга2")
	text_property3		= models.TextField("Услуга3")

