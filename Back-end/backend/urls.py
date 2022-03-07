from django.conf.urls import url
from django.urls import path
from backend import views
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
urlpatterns=[

      url(r'^t1073161h$',csrf_exempt(views.T1073161hsView.as_view()),name='t1073161h'),
      url(r'^t1073161h/(?P<id>\d+)$',csrf_exempt(views.T1073161hsView.as_view()),name='t1073161h'),
      url(r'^t29311hval$',csrf_exempt(views.T29311hvalsView.as_view()),name='t29311hval'),
      url(r'^t29311hval/(?P<id>\d+)$',csrf_exempt(views.T29311hvalsView.as_view()),name='t29311hval'),
      url(r'^t29311h$',csrf_exempt(views.T29311hsView.as_view()),name='t29311h'),
      url(r'^t29311h/(?P<id>\d+)$',csrf_exempt(views.T29311hsView.as_view()),name='t29311h'),   
      url(r'^caleva$',csrf_exempt(views.CalView.as_view()),name='caleva'),
]