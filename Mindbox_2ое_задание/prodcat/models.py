from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	categories = models.ManyToManyField('Category')

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)

	def __str__(self):
		return self.name
