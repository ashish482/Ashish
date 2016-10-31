from django.conf.urls import url,include
from mobile.views import *


urlpatterns=[
     #http://localhost:8080/mobile/api/func_hello_
     url(r'^api/func_hello/?$',func_hello), 
     url(r'^api/newapi/?$',newapi),
     url(r'^api/age/?$',age),
     url(r'^api/mathoperation/?$',mathoperation),
    #url(r'^api/Mathoperation/?$',Mathoperation.as_view()),
]
