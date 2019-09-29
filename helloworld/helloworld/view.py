#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'hello,Messi!'
	context['nameList'] = ['name1','name2','name3','name4','name5']
	return render(request,'hello.html',context)