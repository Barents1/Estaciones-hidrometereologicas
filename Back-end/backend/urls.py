from django.conf.urls import url
from django.urls import path
from backend import views
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
urlpatterns=[

      url(r'^v1073161h$',csrf_exempt(views.V1073161hsApi.as_view()),name='v1073161h'),
      url(r'^v1073161h/(?P<id>\d+)$',csrf_exempt(views.V1073161hsApi.as_view()),name='v1073161h'),
      url(r'^v29311hval$',csrf_exempt(views.V29311hvalsApi.as_view()),name='v29311hval'),
      url(r'^v29311hval/(?P<id>\d+)$',csrf_exempt(views.V29311hvalsApi.as_view()),name='v29311hval'),
      url(r'^v29311h$',csrf_exempt(views.V29311hsApi.as_view()),name='v29311h'),
      url(r'^v29311h/(?P<id>\d+)$',csrf_exempt(views.V29311hsApi.as_view()),name='v29311h'),   
  
]