from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from shop.models import Product, Category


def index(request):
    text_var = 'This is my'
    return HttpResponse(text_var)


def allProdCat(request, c_slug=None):
	c_page = None
	products = None
	if c_slug!=None:
		c_page = get_object_or_404(Category,slug=c_slug)
		products = Product.objects.filter(category=c_page,available=True)
	else:
		products_list = Product.objects.all().filter(available=True)
	# '''Pagination code'''
	# paginator = Paginator(products_list, 6)
	# try:
	# 	page = int(request.GET.get('page','1'))
	# except:
	# 	page = 1
	# try:
	# 	products = paginator.page(page)
	# except (EmptyPage,InvalidPage):
	# 	products = paginator.page(paginator.num_pages)
	return render(request,'shop/category.html',{'category':c_page,'products':products})
