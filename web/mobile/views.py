from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template import Context,loader
from django.views.decorators.csrf import csrf_exempt

import json
import csv

def func_hello(request):
	res='hello world response using function view'
	return HttpResponse(res)
def newapi(request):
	res={}
	sum=''
	try:
	    num1=int(request.GET['num1'])
	    num2=int(request.GET['num2'])

	    sum=num1+num2
	    status='Success'
        except Exception as e:
	    status='Failure,Error:'+str(e)
	res['sum']=sum
	res['status']=status

	return HttpResponse(json.dumps(res))
def age(request):
	res={}
	try:
	    name=(request.GET['name'])
	    gender=(request.GET['gender'])
            status='Success'
        except Exception as e:
            status='Failure,Error:'+str(e)
        res['name']=name
	res['gender']=gender
	res['status']=status
	return HttpResponse(json.dumps(res))

def mathoperation(request):
	res={}
	try:
	    num=int(request.GET['num'])

	    res['square']=num**2
            res['cube']=num**3
	    res['fourth pow']=num**4
	    res['fifth pow']=num**5
	    status='Success'
	except Exception as e:
	    status='Failure,Error:'+str(e)
	res['status']=status
	return HttpResponse(json.dumps(res))

def send_mail(request):
	res={}
	try:
	    filepath=/home/ashish/Desktop/file.txt
