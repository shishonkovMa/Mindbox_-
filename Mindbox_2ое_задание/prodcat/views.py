from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from django.http import HttpResponse
import json


class ProductAPIView(generics.ListAPIView):
	queryset = Product.objects.raw('''
									select
										id,
								 		prodcat_product.name,
										(select 
										    GROUP_CONCAT(prodcat_category.name, ", ")
										from 
										   	prodcat_category, prodcat_product_categories
										where 
										   	prodcat_category.id=prodcat_product_categories.category_id
											and prodcat_product_categories.product_id=prodcat_product.id)
								 	from prodcat_product;''')
	serializer_class = ProductSerializer


class CategoryAPIView(generics.ListAPIView):
	queryset = Category.objects.raw('''
									select
										id,
										prodcat_category.name, 
										(select GROUP_CONCAT(prodcat_product.name, ", ")
										from 
											prodcat_product, prodcat_product_categories
										where 
											prodcat_product.id=prodcat_product_categories.product_id
											and prodcat_product_categories.category_id=prodcat_category.id)
									from prodcat_category;''')
	serializer_class = CategorySerializer


def PairAPIView(request):
	sql = '''
			SELECT
				pp.id,
				pp.name,
				pc.name
			FROM
				prodcat_product_categories ppc
				LEFT JOIN prodcat_product pp on pp.id = ppc.product_id
				LEFT JOIN prodcat_category pc on pc.id = ppc.category_id;'''
	qs = Product.objects.raw(sql)
	list_of_dicts = [model_to_dict(l) for l in qs]
	qs_list = []
	uniq = set()
	for i in list_of_dicts:
		if dict(i)['name'] not in uniq:
			for c in dict(i)['categories']:
				qs_list.append({dict(i)['name']: str(c)})
				uniq.add(dict(i)['name'])
	json_qs = json.dumps(qs_list, ensure_ascii=False)
	return HttpResponse(json_qs, content_type='application/json')
