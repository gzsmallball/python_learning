from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from . import view,testdb,search

urlpatterns = [
	url(r'admin',admin.site.urls),
	url(r'^$',view.hello),
	url(r'insert$',testdb.insert),
	url(r'select$',testdb.select),
	url(r'update$',testdb.update),
	url(r'delete$',testdb.delete),
	url(r'search_form$',search.search_form),
	url(r'search$',search.search),
	url(r'search-post$',search.search_post),
	path('<int:employee_firstname>',testdb.vote,name='vote'),
]