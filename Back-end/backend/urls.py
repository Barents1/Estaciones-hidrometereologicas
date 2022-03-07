from django.conf.urls import url
from django.urls import path
from backend import views
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
urlpatterns=[
      """
            url(r'^t1073161h$',csrf_exempt(views.T1073161hsView.as_view()),name='t1073161h'),
            url(r'^t1073161h/(?P<id>\d+)$',csrf_exempt(views.T1073161hsView.as_view()),name='t1073161h'),
            url(r'^t29311hval$',csrf_exempt(views.T29311hvalsView.as_view()),name='t29311hval'),
            url(r'^t29311hval/(?P<id>\d+)$',csrf_exempt(views.T29311hvalsView.as_view()),name='t29311hval'),
            url(r'^t29311h$',csrf_exempt(views.T29311hsView.as_view()),name='t29311h'),
            url(r'^t29311h/(?P<id>\d+)$',csrf_exempt(views.T29311hsView.as_view()),name='t29311h'),   
            url(r'^caleva$',csrf_exempt(views.CalView.as_view()),name='caleva'),
      """
   
    path('admin/', admin.site.urls),
    path('t1073161h/', views.T1073161hsView.as_view(), name='t1073161h'),
    path('t1073161h/<int:id>',views.T1073161hsView.as_view(),name='t1073161h')
    path('t29311hval/', views.T29311hvalsView.as_view(),name='t29311hval'),
    path('t29311hval/<int:id>',views.T29311hvalsView.as_view(),name='t29311hval')
    path('t29311h/', views.T29311hsView.as_view(),name='t29311h'),
    path('t29311h/<int:id>',views.T29311hsView.as_view(),name='t29311h'),
    path('caleva/',views.CalView.as_view(),name='caleva'),


]