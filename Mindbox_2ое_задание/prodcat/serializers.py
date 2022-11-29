from rest_framework import serializers
from .models import *


class ListingField(serializers.RelatedField):
     def to_representation(self, value):
         return value.name


class ProductSerializer(serializers.ModelSerializer):
	categories = ListingField(many=True, read_only=True)
	product_name = serializers.CharField(source='name')

	class Meta:
		model = Product
		fields = ('product_name', 'categories')


class CategorySerializer(serializers.ModelSerializer):
	product_set = ProductSerializer(many=True, read_only=True)
	product_set = ListingField(many=True, read_only=True)
	category_name = serializers.CharField(source='name')

	class Meta:
		model = Category
		fields = ['category_name', 'product_set']


# class PairSerializer(serializers.ModelSerializer):
# 	data = serializers.serialize('json', UserMcqAnswer.objects.raw(queryset), fields='__all__')
	# product_set = ProductSerializer(many=False, read_only=True)
# 	# profile_picture = UserProfilePicture(source='profile_picture', read_only=True)
# 	# product_name = ProductSerializer(read_only=True)
# 	name = serializers.SerializerMethodField(source='name', read_only=True)
# 	category_name = serializers.CharField(source='name')

	# class Meta:
	# 	model = Category
	# 	fields = '__all__'#('product_name', 'category_name')
