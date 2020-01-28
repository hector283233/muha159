from django.db import models

class Group(models.Model):
	TYPES = (
				('DG', 'Demir Gapylar'),
				('AG', 'Agaç Gapylar'),
				('MB', 'Mebeller'),
				('DO', 'Demir Önümler'),
				('BK', 'Beýlekiler'),
			)
	group_name			= models.CharField("Gruppanyn ady", max_length=128)
	group_type			= models.CharField("Topary", max_length=2, choices=TYPES)

	def __str__(self):
		return self.group_name
			

class Product(models.Model):
	product_name		= models.CharField("Harydyň ady", max_length=128)
	product_group		= models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name="Gruppasy")
	product_image 		= models.ImageField("Haryt Suraty", upload_to = 'images/', default = 'images/default.jpg')
	product_description = models.TextField("Haryt Barada Giňişleýin Maglumat")
	is_new				= models.BooleanField("Täzemi?", default=1)

	def __str__(self):
		return self.product_name

class Main_Page(models.Model):
	img_slide1 			= models.ImageField("Slayt1", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide2 			= models.ImageField("Slayt2", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide3 			= models.ImageField("Slayt3", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide4 			= models.ImageField("Slayt4", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide5 			= models.ImageField("Slayt5", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide6 			= models.ImageField("Slayt6", upload_to = 'furnitures/images/', default = 'default.jpg')

	text_slide1 		= models.CharField("Slayt1 tekst", max_length=32)
	text_slide2 		= models.CharField("Slayt2 tekst", max_length=32)
	text_slide3 		= models.CharField("Slayt3 tekst", max_length=32)
	text_slide4 		= models.CharField("Slayt4 tekst", max_length=32)
	text_slide5 		= models.CharField("Slayt5 tekst", max_length=32)
	text_slide6 		= models.CharField("Slayt6 tekst", max_length=32)

	description_slide1 	= models.TextField("Slayt1 Giňişleýin")
	description_slide2 	= models.TextField("Slayt2 Giňişleýin")
	description_slide3 	= models.TextField("Slayt3 Giňişleýin")
	description_slide4 	= models.TextField("Slayt4 Giňişleýin")
	description_slide5 	= models.TextField("Slayt5 Giňişleýin")
	description_slide6 	= models.TextField("Slayt6 Giňişleýin")

	company_name 		= models.CharField("Kärhananyň ady", max_length=64)

	about_company		= models.TextField('Kärhana Barada Giňişleýin')

	property1			= models.ImageField("Icon1", upload_to = 'furnitures/images/', default = 'default.jpg')
	property2			= models.ImageField("Icon2", upload_to = 'furnitures/images/', default = 'default.jpg')
	property3			= models.ImageField("Icon3", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property1		= models.TextField("Hyzmat1")
	text_property2		= models.TextField("Hyzmat2")
	text_property3		= models.TextField("Hyzmat3")

