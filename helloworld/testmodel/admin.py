from django.contrib import admin
from testmodel.models import Test,Contact,Tag,Employee

# Register your models here.

class TagInline(admin.TabularInline):
	model = Tag

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name','age','email')
	search_fields = ('name','email','age')
	inlines = [TagInline]
	fieldsets = (
		['Main',{
			'fields':('name','email')
		}],
		['Advance',{
			'classes':('collapse',),
			'fields':('age',)
		}]
	)

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','age','sex','income')
	
admin.site.register(Contact,ContactAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register([Test,Tag,])