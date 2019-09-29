from django.http import HttpResponse
from django.shortcuts import render

from testmodel.models import Test

def insert(request):
	test1 = Test(name='runoob1')
	test1.save()
	test2 = Test(name='runoob2')
	test2.save()
	
	return HttpResponse('<p>Succesfully insert the data !</p>')

def select(request):
	response = ''
	response1 = ''
	
	list = Test.objects.filter(name='runoob2').order_by('id')
	response2 = Test.objects.filter(id=1)
	response3 = Test.objects.get(id=1)
	
	for var in list:
		response1 += var.name + ' '
	
	response = response1
	
	return render(request,'showselect.html',{'nameList':list})

def update(request):
	Test.objects.filter(id=3).update(name='google')
	return HttpResponse('<p> update ! </p>')

def delete(request):
	Test.objects.get(id=4).delete()
	return 	HttpResponse('<p>delete</p>')

def vote(request,employee_firstname):
	return HttpResponse("your're looking for employee : %s" % employee_firstname)