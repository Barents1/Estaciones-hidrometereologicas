import datetime
from decimal import Decimal
from pyexpat import model

from re import template
from urllib import response
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.utils import json
from rest_framework.relations import method_overridden
from backend.models import *
from backend.serializers import *
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Q 
from django import forms
class Calculos():

     
     def precipitacion_1714161h(self):
          

         
         


           T1714161hs.id_estacion = 4
           T1714161hs.id_unidad_medida = 4
           T1714161hs.id_usuario = 0
           T1714161hs.fecha_toma = "2022-03-08 13:00:00"
           T1714161hs.fecha_ingreso = "2022-03-08 13:00:00"
          


           fecha="2022-03-08"
           fechadiasiguiente="2022-03-09"
           valor13h =T1714161hs.objects.filter(fecha_toma__range=(fecha+" 13:00:00",fecha+" 13:59:59")).values('valor')
           valor19h =T1714161hs.objects.filter(fecha_toma__range=(fecha+" 19:00:00",fecha+" 19:59:59")).values('valor')
           valor07hdiasiguiente =T1714161hs.objects.filter(fecha_toma__range=(fechadiasiguiente+" 07:00:00",fechadiasiguiente+" 07:59:59")).values('valor')
          
           if valor13h.exists()==True :
               for a in valor13h:
                    valor1=a['valor']
           else:
                valor1='no existe valor 13 horas '
                return (valor1)

           if valor19h.exists()==True :
               for a in valor19h:
                    valor2=a['valor']
           else:
                valor2='no existe valor 19 horas'
                return (valor2)

           if valor07hdiasiguiente.exists()==True :
               for a in valor07hdiasiguiente:
                    valor3=a['valor']
           else:
                valor3='no existe valor 07 horas dia siguiente'
                return (valor3)
          

           T1714161hs.valor=valor1+valor2+valor3

           T1714161hs.save()
           return (4)

class DatosCalculos():

     def resul(self):
          calcular = Calculos()
          calcular.precipitacion_1714161h()


class T171481hp():
      
    def post(self,request):
         
         t171481h_data=JSONParser().parse(request)
         t171481h_serializer=T171481hSerializer(data=t171481h_data)
         if t171481h_serializer.is_valid():
             t171481h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t171481hs = T171481hs.objects.all()
         t171481h_serializer=T171481hSerializer(t171481hs,many=True)
         return JsonResponse(t171481h_serializer.data,safe=False)

    def put(self,request):
         t171481h_data=JSONParser().parse(request)
         t171481h=T171481hs.objects.get(id_prec=t171481h_data['id_prec'])
         t171481h_serializer=T1073161hSerializer(t171481h,data=t171481h_data)
         if t171481h_serializer.is_valid():
            t171481h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t171481h=T171481hs.objects.get(id_prec=id)
        t171481h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T1073161hsView(View):
     
      
     def post(self,request):
          datoscal = Calculos()
          print(datoscal.precipitacion_1714161h())
          t1073161h_data=JSONParser().parse(request)
          t1073161h_serializer=T1073161hSerializer(data=t1073161h_data)
          if t1073161h_serializer.is_valid():
               t1073161h_serializer.save()
               return JsonResponse('Se agrrego correctamente',safe=False)
          return   JsonResponse('No se pudo agregar ',safe=False) 
     
     def get(self,request):
          
          t1073161hs = T1073161hs.objects.all()
          t1073161h_serializer=T1073161hSerializer(t1073161hs,many=True)
          return JsonResponse(t1073161h_serializer.data,safe=False)


     def put(self,request):
          t1073161h_data=JSONParser().parse(request)
          t1073161h=T1073161hs.objects.get(id_temp_int_baro=t1073161h_data['id_temp_int_baro'])
          t1073161h_serializer=T1073161hSerializer(t1073161h,data=t1073161h_data)
          if t1073161h_serializer.is_valid():
               t1073161h_serializer.save()
               return JsonResponse("Updated Successfully",safe=False)
          return JsonResponse("Failed to Update")

     def delete(self,request,id):
          t1073161h=T1073161hs.objects.get(id_temp_int_baro=id)
          t1073161h.delete()
          return JsonResponse("Deleted Successfully",safe=False)
     
class T1073161hvalsView(View):
     
     def post(self,request):
          t1073161hval_data=JSONParser().parse(request)
          t1073161hval_serializer=T1073161hvalSerializer(data=t1073161hval_data)
          if t1073161hval_serializer.is_valid():
               t1073161hval_serializer.save()
               return JsonResponse('Se agrrego correctamente',safe=False)
          return   JsonResponse('No se pudo agregar ',safe=False) 
     
     def get(self,request):
          t1073161hvals = T1073161hvals.objects.all()
          t1073161hval_serializer=T1073161hvalSerializer(t1073161hvals,many=True)
          return JsonResponse(t1073161hval_serializer.data,safe=False)

     def put(self,request):
          t1073161hval_data=JSONParser().parse(request)
          t1073161hval=T1073161hvals.objects.get(id_temp_int_baro_val=t1073161hval_data['id_temp_int_baro_val'])
          t1073161hval_serializer=T1073161hSerializer(t1073161hval,data=t1073161hval_data)
          if t1073161hval_serializer.is_valid():
               t1073161hval_serializer.save()
               return JsonResponse("Updated Successfully",safe=False)
          return JsonResponse("Failed to Update")

     def delete(self,request,id):
          t1073161hval=T1073161hvals.objects.get(id_temp_int_baro_val=id)
          t1073161hval.delete()
          return JsonResponse("Deleted Successfully",safe=False)


class T1087161hsView(View):
      
    def post(self,request):
         t1087161h_data=JSONParser().parse(request)
         t1087161h_serializer=T1087161hSerializer(data=t1087161h_data)
         if t1087161h_serializer.is_valid():
             t1087161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1087161hs = T1087161hs.objects.all()
         t1087161h_serializer=T1087161hSerializer(t1087161hs,many=True)
         return JsonResponse(t1087161h_serializer.data,safe=False)

    def put(self,request):
         t1087161h_data=JSONParser().parse(request)
         t1087161h=T1087161hs.objects.get(id_pres_corre=t1087161h_data['id_temp_int_baro_val'])
         t1087161h_serializer=T1087161hSerializer(t1087161h,data=t1087161h_data)
         if t1087161h_serializer.is_valid():
            t1087161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1087161h=T1087161hs.objects.get(id_pres_corre=id)
        t1087161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)


class T1087161hvalsView(View):
      
    def post(self,request):
         t1087161hval_data=JSONParser().parse(request)
         t1087161hval_serializer=T1087161hvalSerializer(data=t1087161hval_data)
         if t1087161hval_serializer.is_valid():
             t1087161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1087161hvals = T1087161hvals.objects.all()
         t1087161hval_serializer=T1087161hvalSerializer(t1087161hvals,many=True)
         return JsonResponse(t1087161hval_serializer.data,safe=False)

    def put(self,request):
         t1087161hval_data=JSONParser().parse(request)
         t1087161hval=T1087161hvals.objects.get(id_pres_corre_val=t1087161hval_data['id_temp_int_baro_val'])
         t1087161hval_serializer=T1073161hSerializer(t1087161hval,data=t1087161hval_data)
         if t1087161hval_serializer.is_valid():
            t1087161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1087161hval=T1087161hvals.objects.get(id_pres_corre_val=id)
        t1087161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False) 

class T1097161hsView(View):
      
    def post(self,request):
         
         t1097161h_data=JSONParser().parse(request)
         t1097161h_serializer=T1097161hSerializer(data=t1097161h_data)
         if t1097161h_serializer.is_valid():
             t1097161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1097161hs = T1097161hs.objects.all()
         t1097161h_serializer=T1097161hSerializer(t1097161hs,many=True)
         return JsonResponse(t1097161h_serializer.data,safe=False)

    def put(self,request):
         t1097161h_data=JSONParser().parse(request)
         t1097161h=T1097161hs.objects.get(id_pres_cont=t1097161h_data['id_pres_cont'])
         t1097161h_serializer=T1073161hSerializer(t1097161h,data=t1097161h_data)
         if t1097161h_serializer.is_valid():
            t1097161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1097161h=T1097161hs.objects.get(id_pres_cont=id)
        t1097161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)        


class T1097161hvalsView(View):
      
    def post(self,request):
         
         t1097161hval_data=JSONParser().parse(request)
         t1097161hval_serializer=T1097161hvalSerializer(data=t1097161hval_data)
         if t1097161hval_serializer.is_valid():
             t1097161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1097161hvals = T1097161hvals.objects.all()
         t1097161hval_serializer=T1097161hvalSerializer(t1097161hvals,many=True)
         return JsonResponse(t1097161hval_serializer.data,safe=False)

    def put(self,request):
         t1097161hval_data=JSONParser().parse(request)
         t1097161hval=T1097161hvals.objects.get(id_pres_cont_val=t1097161hval_data['id_pres_cont_val'])
         t1097161hval_serializer=T1073161hSerializer(t1097161hval,data=t1097161hval_data)
         if t1097161hval_serializer.is_valid():
            t1097161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1097161hval=T1097161hvals.objects.get(id_pres_cont_val=id)
        t1097161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)      


class T1263011hsView(View):
      
    def post(self,request):
         
         t1263011h_data=JSONParser().parse(request)
         t1263011h_serializer=T1263011hSerializer(data=t1263011h_data)
         if t1263011h_serializer.is_valid():
             t1263011h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1263011hs = T1263011hs.objects.all()
         t1263011h_serializer=T1263011hSerializer(t1263011hs,many=True)
         return JsonResponse(t1263011h_serializer.data,safe=False)

    def put(self,request):
         t1263011h_data=JSONParser().parse(request)
         t1263011h=T1263011hs.objects.get(id_caudal_max_hor=t1263011h_data['id_caudal_max_hor'])
         t1263011h_serializer=T1073161hSerializer(t1263011h,data=t1263011h_data)
         if t1263011h_serializer.is_valid():
            t1263011h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1263011h=T1263011hs.objects.get(id_caudal_max_hor=id)
        t1263011h.delete()
        return JsonResponse("Deleted Successfully",safe=False)      


class T1263011hvalsView(View):
      
    def post(self,request):
         
         t1263011hval_data=JSONParser().parse(request)
         t1263011hval_serializer=T1263011hvalSerializer(data=t1263011hval_data)
         if t1263011hval_serializer.is_valid():
             t1263011hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1263011hvals = T1263011hvals.objects.all()
         t1263011hval_serializer=T1263011hvalSerializer(t1263011hvals,many=True)
         return JsonResponse(t1263011hval_serializer.data,safe=False)

    def put(self,request):
         t1263011hval_data=JSONParser().parse(request)
         t1263011hval=T1263011hvals.objects.get(id_caudal_max_hor_val=t1263011hval_data['id_caudal_max_hor_val'])
         t1263011hval_serializer=T1073161hSerializer(t1263011hval,data=t1263011hval_data)
         if t1263011hval_serializer.is_valid():
            t1263011hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1263011hval=T1263011hvals.objects.get(id_caudal_max_hor_val=id)
        t1263011hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T12630161hsView(View):
      
    def post(self,request):
         
         t12630161h_data=JSONParser().parse(request)
         t12630161h_serializer=T12630161hSerializer(data=t12630161h_data)
         if t12630161h_serializer.is_valid():
             t12630161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t12630161hs = T12630161hs.objects.all()
         t12630161h_serializer=T12630161hSerializer(t12630161hs,many=True)
         return JsonResponse(t12630161h_serializer.data,safe=False)

    def put(self,request):
         t12630161h_data=JSONParser().parse(request)
         t12630161h=T12630161hs.objects.get(id_caudal_ins_hor=t12630161h_data['id_caudal_ins_hor'])
         t12630161h_serializer=T1073161hSerializer(t12630161h,data=t12630161h_data)
         if t12630161h_serializer.is_valid():
            t12630161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t12630161h=T12630161hs.objects.get(id_caudal_ins_hor=id)
        t12630161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class T12630161hvalsView(View):
      
    def post(self,request):
         
         t12630161hval_data=JSONParser().parse(request)
         t12630161hval_serializer=T12630161hvalSerializer(data=t12630161hval_data)
         if t12630161hval_serializer.is_valid():
             t12630161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t12630161hvals = T12630161hvals.objects.all()
         t12630161hval_serializer=T12630161hvalSerializer(t12630161hvals,many=True)
         return JsonResponse(t12630161hval_serializer.data,safe=False)

    def put(self,request):
         t12630161hval_data=JSONParser().parse(request)
         t12630161hval=T12630161hvals.objects.get(id_caudal_ins_hor_val=t12630161hval_data['id_caudal_ins_hor_val'])
         t12630161hval_serializer=T1073161hSerializer(t12630161hval,data=t12630161hval_data)
         if t12630161hval_serializer.is_valid():
            t12630161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t12630161hval=T12630161hvals.objects.get(id_caudal_ins_hor_val=id)
        t12630161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False) 


class T1263021hsView(View):
      
    def post(self,request):
         
         t1263021h_data=JSONParser().parse(request)
         t1263021h_serializer=T1263021hSerializer(data=t1263021h_data)
         if t1263021h_serializer.is_valid():
             t1263021h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1263021hs = T1263021hs.objects.all()
         t1263021h_serializer=T1263021hSerializer(t1263021hs,many=True)
         return JsonResponse(t1263021h_serializer.data,safe=False)

    def put(self,request):
         t1263021h_data=JSONParser().parse(request)
         t1263021h=T1263021hs.objects.get(id_caudal_min_hor=t1263021h_data['id_caudal_min_hor'])
         t1263021h_serializer=T1073161hSerializer(t1263021h,data=t1263021h_data)
         if t1263021h_serializer.is_valid():
            t1263021h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1263021h=T1263021hs.objects.get(id_caudal_min_hor=id)
        t1263021h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     



class T1263021hvalsView(View):
      
    def post(self,request):
         
         t1263021hval_data=JSONParser().parse(request)
         t1263021hval_serializer=T1263021hvalSerializer(data=t1263021hval_data)
         if t1263021hval_serializer.is_valid():
             t1263021hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1263021hvals = T1263021hvals.objects.all()
         t1263021hval_serializer=T1263021hvalSerializer(t1263021hvals,many=True)
         return JsonResponse(t1263021hval_serializer.data,safe=False)

    def put(self,request):
         t1263021hval_data=JSONParser().parse(request)
         t1263021hval=T1263021hvals.objects.get(id_caudal_min_hor_val=t1263021hval_data['id_caudal_min_hor_val'])
         t1263021hval_serializer=T1073161hSerializer(t1263021hval,data=t1263021hval_data)
         if t1263021hval_serializer.is_valid():
            t1263021hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1263021hval=T1263021hvals.objects.get(id_caudal_min_hor_val=id)
        t1263021hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T1263041hsView(View):
      
    def post(self,request):
         
         t1263041h_data=JSONParser().parse(request)
         t1263041h_serializer=T1263041hSerializer(data=t1263041h_data)
         if t1263041h_serializer.is_valid():
             t1263041h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1263041hs = T1263041hs.objects.all()
         t1263041h_serializer=T1263041hSerializer(t1263041hs,many=True)
         return JsonResponse(t1263041h_serializer.data,safe=False)

    def put(self,request):
         t1263041h_data=JSONParser().parse(request)
         t1263041h=T1263041hs.objects.get(id_caudal_prom_hor=t1263041h_data['id_caudal_prom_hor'])
         t1263041h_serializer=T1073161hSerializer(t1263041h,data=t1263041h_data)
         if t1263041h_serializer.is_valid():
            t1263041h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1263041h=T1263041hs.objects.get(id_caudal_prom_hor=id)
        t1263041h.delete()
        return JsonResponse("Deleted Successfully",safe=False)


class T1263041hvalsView(View):
      
    def post(self,request):
         
         t1263041hval_data=JSONParser().parse(request)
         t1263041hval_serializer=T1263041hvalSerializer(data=t1263041hval_data)
         if t1263041hval_serializer.is_valid():
             t1263041hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1263041hvals = T1263041hvals.objects.all()
         t1263041hval_serializer=T1263041hvalSerializer(t1263041hvals,many=True)
         return JsonResponse(t1263041hval_serializer.data,safe=False)

    def put(self,request):
         t1263041hval_data=JSONParser().parse(request)
         t1263041hval=T1263041hvals.objects.get(id_caudal_prom_hor_val=t1263041hval_data['id_caudal_prom_hor_val'])
         t1263041hval_serializer=T1073161hSerializer(t1263041hval,data=t1263041hval_data)
         if t1263041hval_serializer.is_valid():
            t1263041hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1263041hval=T1263041hvals.objects.get(id_caudal_prom_hor_val=id)
        t1263041hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  



class T141011hsView(View):
      
    def post(self,request):
         
         t141011h_data=JSONParser().parse(request)
         t141011h_serializer=T141011hSerializer(data=t141011h_data)
         if t141011h_serializer.is_valid():
             t141011h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t141011hs = T141011hs.objects.all()
         t141011h_serializer=T141011hSerializer(t141011hs,many=True)
         return JsonResponse(t141011h_serializer.data,safe=False)

    def put(self,request):
         t141011h_data=JSONParser().parse(request)
         t141011h=T141011hs.objects.get(id_nitelagua_max_hor=t141011h_data['id_nitelagua_max_hor'])
         t141011h_serializer=T1073161hSerializer(t141011h,data=t141011h_data)
         if t141011h_serializer.is_valid():
            t141011h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t141011h=T141011hs.objects.get(id_nitelagua_max_hor=id)
        t141011h.delete()
        return JsonResponse("Deleted Successfully",safe=False)          




class T141011hvalsView(View):
      
    def post(self,request):
         
         t141011hval_data=JSONParser().parse(request)
         t141011hval_serializer=T141011hvalSerializer(data=t141011hval_data)
         if t141011hval_serializer.is_valid():
             t141011hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t141011hvals = T141011hvals.objects.all()
         t141011hval_serializer=T141011hvalSerializer(t141011hvals,many=True)
         return JsonResponse(t141011hval_serializer.data,safe=False)

    def put(self,request):
         t141011hval_data=JSONParser().parse(request)
         t141011hval=T141011hvals.objects.get(id_nitelagua_max_hor_val=t141011hval_data['id_nitelagua_max_hor_val'])
         t141011hval_serializer=T1073161hSerializer(t141011hval,data=t141011hval_data)
         if t141011hval_serializer.is_valid():
            t141011hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t141011hval=T141011hvals.objects.get(id_nitelagua_max_hor_val=id)
        t141011hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T1410161hsView(View):
      
    def post(self,request):
         
         t1410161h_data=JSONParser().parse(request)
         t1410161h_serializer=T1410161hSerializer(data=t1410161h_data)
         if t1410161h_serializer.is_valid():
             t1410161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1410161hs = T1410161hs.objects.all()
         t1410161h_serializer=T1410161hSerializer(t1410161hs,many=True)
         return JsonResponse(t1410161h_serializer.data,safe=False)

    def put(self,request):
         t1410161h_data=JSONParser().parse(request)
         t1410161h=T1410161hs.objects.get(id_nitelagua_ins_hor=t1410161h_data['id_nitelagua_ins_hor'])
         t1410161h_serializer=T1073161hSerializer(t1410161h,data=t1410161h_data)
         if t1410161h_serializer.is_valid():
            t1410161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1410161h=T1410161hs.objects.get(id_nitelagua_ins_hor=id)
        t1410161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T1410161hvalsView(View):
      
    def post(self,request):
         
         t1410161hval_data=JSONParser().parse(request)
         t1410161hval_serializer=T1410161hvalSerializer(data=t1410161hval_data)
         if t1410161hval_serializer.is_valid():
             t1410161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1410161hvals = T1410161hvals.objects.all()
         t1410161hval_serializer=T1410161hvalSerializer(t1410161hvals,many=True)
         return JsonResponse(t1410161hval_serializer.data,safe=False)

    def put(self,request):
         t1410161hval_data=JSONParser().parse(request)
         t1410161hval=T1410161hvals.objects.get(id_nitelagua_ins_hor_val=t1410161hval_data['id_nitelagua_ins_hor_val'])
         t1410161hval_serializer=T1073161hSerializer(t1410161hval,data=t1410161hval_data)
         if t1410161hval_serializer.is_valid():
            t1410161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1410161hval=T1410161hvals.objects.get(id_nitelagua_ins_hor_val=id)
        t1410161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T141021hsView(View):
      
    def post(self,request):
         
         t141021h_data=JSONParser().parse(request)
         t141021h_serializer=T141021hSerializer(data=t141021h_data)
         if t141021h_serializer.is_valid():
             t141021h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t141021hs = T141021hs.objects.all()
         t141021h_serializer=T141021hSerializer(t141021hs,many=True)
         return JsonResponse(t141021h_serializer.data,safe=False)

    def put(self,request):
         t141021h_data=JSONParser().parse(request)
         t141021h=T141021hs.objects.get(id_nitelagua_min_hor=t141021h_data['id_nitelagua_min_hor'])
         t141021h_serializer=T1073161hSerializer(t141021h,data=t141021h_data)
         if t141021h_serializer.is_valid():
            t141021h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t141021h=T141021hs.objects.get(id_nitelagua_min_hor=id)
        t141021h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T141021hvalsView(View):
      
    def post(self,request):
         
         t141021hval_data=JSONParser().parse(request)
         t141021hval_serializer=T141021hvalSerializer(data=t141021hval_data)
         if t141021hval_serializer.is_valid():
             t141021hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t141021hvals = T141021hvals.objects.all()
         t141021hval_serializer=T141021hvalSerializer(t141021hvals,many=True)
         return JsonResponse(t141021hval_serializer.data,safe=False)

    def put(self,request):
         t141021hval_data=JSONParser().parse(request)
         t141021hval=T141021hvals.objects.get(id_nitelagua_min_hor_val=t141021hval_data['id_nitelagua_min_hor_val'])
         t141021hval_serializer=T1073161hSerializer(t141021hval,data=t141021hval_data)
         if t141021hval_serializer.is_valid():
            t141021hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t141021hval=T141021hvals.objects.get(id_nitelagua_min_hor_val=id)
        t141021hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     



class T141041hsView(View):
      
    def post(self,request):
         
         t141041h_data=JSONParser().parse(request)
         t141041h_serializer=T141041hSerializer(data=t141041h_data)
         if t141041h_serializer.is_valid():
             t141041h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t141041hs = T141041hs.objects.all()
         t141041h_serializer=T141041hSerializer(t141041hs,many=True)
         return JsonResponse(t141041h_serializer.data,safe=False)

    def put(self,request):
         t141041h_data=JSONParser().parse(request)
         t141041h=T141041hs.objects.get(id_nitelagua_prom_hor=t141041h_data['id_nitelagua_prom_hor'])
         t141041h_serializer=T1073161hSerializer(t141041h,data=t141041h_data)
         if t141041h_serializer.is_valid():
            t141041h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t141041h=T141041hs.objects.get(id_nitelagua_prom_hor=id)
        t141041h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class T141041hvalsView(View):
      
    def post(self,request):
         
         t141041hval_data=JSONParser().parse(request)
         t141041hval_serializer=T141041hvalSerializer(data=t141041hval_data)
         if t141041hval_serializer.is_valid():
             t141041hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t141041hvals = T141041hvals.objects.all()
         t141041hval_serializer=T141041hvalSerializer(t141041hvals,many=True)
         return JsonResponse(t141041hval_serializer.data,safe=False)

    def put(self,request):
         t141041hval_data=JSONParser().parse(request)
         t141041hval=T141041hvals.objects.get(id_nitelagua_prom_hor_val=t141041hval_data['id_nitelagua_prom_hor_val'])
         t141041hval_serializer=T1073161hSerializer(t141041hval,data=t141041hval_data)
         if t141041hval_serializer.is_valid():
            t141041hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t141041hval=T141041hvals.objects.get(id_nitelagua_prom_hor_val=id)
        t141041hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)   


class T1714161hsView(View):
      
    def post(self,request):
         
         t1714161h_data=JSONParser().parse(request)
         t1714161h_serializer=T1714161hSerializer(data=t1714161h_data)
         if t1714161h_serializer.is_valid():
             t1714161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1714161hs = T1714161hs.objects.all()
         t1714161h_serializer=T1714161hSerializer(t1714161hs,many=True)
         return JsonResponse(t1714161h_serializer.data,safe=False)

    def put(self,request):
         t1714161h_data=JSONParser().parse(request)
         t1714161h=T1714161hs.objects.get(id_prec_1h=t1714161h_data['id_prec_1h'])
         t1714161h_serializer=T1073161hSerializer(t1714161h,data=t1714161h_data)
         if t1714161h_serializer.is_valid():
            t1714161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1714161h=T1714161hs.objects.get(id_prec_1h=id)
        t1714161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)       


class T1714161hvalsView(View):
      
    def post(self,request):
         
         t1714161hval_data=JSONParser().parse(request)
         t1714161hval_serializer=T1714161hvalSerializer(data=t1714161hval_data)
         if t1714161hval_serializer.is_valid():
             t1714161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t1714161hvals = T1714161hvals.objects.all()
         t1714161hval_serializer=T1714161hvalSerializer(t1714161hvals,many=True)
         return JsonResponse(t1714161hval_serializer.data,safe=False)

    def put(self,request):
         t1714161hval_data=JSONParser().parse(request)
         t1714161hval=T1714161hvals.objects.get(id_prec_1h_val=t1714161hval_data['id_prec_1h_val'])
         t1714161hval_serializer=T1073161hSerializer(t1714161hval,data=t1714161hval_data)
         if t1714161hval_serializer.is_valid():
            t1714161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t1714161hval=T1714161hvals.objects.get(id_prec_1h_val=id)
        t1714161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)   


class T171481hsView(View):
      
    def post(self,request):
         
         t171481h_data=JSONParser().parse(request)
         t171481h_serializer=T171481hSerializer(data=t171481h_data)
         if t171481h_serializer.is_valid():
             t171481h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t171481hs = T171481hs.objects.all()
         t171481h_serializer=T171481hSerializer(t171481hs,many=True)
         return JsonResponse(t171481h_serializer.data,safe=False)

    def put(self,request):
         t171481h_data=JSONParser().parse(request)
         t171481h=T171481hs.objects.get(id_prec=t171481h_data['id_prec'])
         t171481h_serializer=T1073161hSerializer(t171481h,data=t171481h_data)
         if t171481h_serializer.is_valid():
            t171481h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t171481h=T171481hs.objects.get(id_prec=id)
        t171481h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T171481hvalsView(View):
      
    def post(self,request):
         
         t171481hval_data=JSONParser().parse(request)
         t171481hval_serializer=T171481hvalSerializer(data=t171481hval_data)
         if t171481hval_serializer.is_valid():
             t171481hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t171481hvals = T171481hvals.objects.all()
         t171481hval_serializer=T171481hvalSerializer(t171481hvals,many=True)
         return JsonResponse(t171481hval_serializer.data,safe=False)

    def put(self,request):
         t171481hval_data=JSONParser().parse(request)
         t171481hval=T171481hvals.objects.get(id_prec_val=t171481hval_data['id_prec_val'])
         t171481hval_serializer=T1073161hSerializer(t171481hval,data=t171481hval_data)
         if t171481hval_serializer.is_valid():
            t171481hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t171481hval=T171481hvals.objects.get(id_prec_val=id)
        t171481hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T187161hsView(View):
      
    def post(self,request):
         
         t187161h_data=JSONParser().parse(request)
         t187161h_serializer=T187161hSerializer(data=t187161h_data)
         if t187161h_serializer.is_valid():
             t187161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t187161hs = T187161hs.objects.all()
         t187161h_serializer=T187161hSerializer(t187161hs,many=True)
         return JsonResponse(t187161h_serializer.data,safe=False)

    def put(self,request):
         t187161h_data=JSONParser().parse(request)
         t187161h=T187161hs.objects.get(id_presion=t187161h_data['id_presion'])
         t187161h_serializer=T1073161hSerializer(t187161h,data=t187161h_data)
         if t187161h_serializer.is_valid():
            t187161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t187161h=T187161hs.objects.get(id_presion=id)
        t187161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T187161hvalsView(View):
      
    def post(self,request):
         
         t187161hval_data=JSONParser().parse(request)
         t187161hval_serializer=T187161hvalSerializer(data=t187161hval_data)
         if t187161hval_serializer.is_valid():
             t187161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t187161hvals = T187161hvals.objects.all()
         t187161hval_serializer=T187161hvalSerializer(t187161hvals,many=True)
         return JsonResponse(t187161hval_serializer.data,safe=False)

    def put(self,request):
         t187161hval_data=JSONParser().parse(request)
         t187161hval=T187161hvals.objects.get(id_presion_val=t187161hval_data['id_presion_val'])
         t187161hval_serializer=T1073161hSerializer(t187161hval,data=t187161hval_data)
         if t187161hval_serializer.is_valid():
            t187161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t187161hval=T187161hvals.objects.get(id_presion_val=id)
        t187161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)       

class T272981hsView(View):
      
    def post(self,request):
         
         t272981h_data=JSONParser().parse(request)
         t272981h_serializer=T272981hSerializer(data=t272981h_data)
         if t272981h_serializer.is_valid():
             t272981h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t272981hs = T272981hs.objects.all()
         t272981h_serializer=T272981hSerializer(t272981hs,many=True)
         return JsonResponse(t272981h_serializer.data,safe=False)

    def put(self,request):
         t272981h_data=JSONParser().parse(request)
         t272981h=T272981hs.objects.get(id_tiento_rec=t272981h_data['id_tiento_rec'])
         t272981h_serializer=T1073161hSerializer(t272981h,data=t272981h_data)
         if t272981h_serializer.is_valid():
            t272981h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t272981h=T272981hs.objects.get(id_tiento_rec=id)
        t272981h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T272981hvalsView(View):
      
    def post(self,request):
         
         t272981hval_data=JSONParser().parse(request)
         t272981hval_serializer=T272981hvalSerializer(data=t272981hval_data)
         if t272981hval_serializer.is_valid():
             t272981hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t272981hvals = T272981hvals.objects.all()
         t272981hval_serializer=T272981hvalSerializer(t272981hvals,many=True)
         return JsonResponse(t272981hval_serializer.data,safe=False)

    def put(self,request):
         t272981hval_data=JSONParser().parse(request)
         t272981hval=T272981hvals.objects.get(id_tiento_rec_val=t272981hval_data['id_tiento_rec_val'])
         t272981hval_serializer=T1073161hSerializer(t272981hval,data=t272981hval_data)
         if t272981hval_serializer.is_valid():
            t272981hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t272981hval=T272981hvals.objects.get(id_tiento_rec_val=id)
        t272981hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T29311hsView(View):
      
    def post(self,request):
         
         t29311h_data=JSONParser().parse(request)
         t29311h_serializer=T29311hSerializer(data=t29311h_data)
         if t29311h_serializer.is_valid():
             t29311h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t29311hs = T29311hs.objects.all()
         t29311h_serializer=T29311hSerializer(t29311hs,many=True)
         return JsonResponse(t29311h_serializer.data,safe=False)

    def put(self,request):
         t29311h_data=JSONParser().parse(request)
         t29311h=T29311hs.objects.get(id_temp_aire_max=t29311h_data['id_temp_aire_max'])
         t29311h_serializer=T1073161hSerializer(t29311h,data=t29311h_data)
         if t29311h_serializer.is_valid():
            t29311h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t29311h=T29311hs.objects.get(id_temp_aire_max=id)
        t29311h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T29311hvalsView(View):
      
    def post(self,request):
         
         t29311hval_data=JSONParser().parse(request)
         t29311hval_serializer=T29311hvalSerializer(data=t29311hval_data)
         if t29311hval_serializer.is_valid():
             t29311hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t29311hvals = T29311hvals.objects.all()
         t29311hval_serializer=T29311hvalSerializer(t29311hvals,many=True)
         return JsonResponse(t29311hval_serializer.data,safe=False)

    def put(self,request):
         t29311hval_data=JSONParser().parse(request)
         t29311hval=T29311hvals.objects.get(id_temp_aire_max_val=t29311hval_data['id_temp_aire_max_val'])
         t29311hval_serializer=T1073161hSerializer(t29311hval,data=t29311hval_data)
         if t29311hval_serializer.is_valid():
            t29311hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t29311hval=T29311hvals.objects.get(id_temp_aire_max_val=id)
        t29311hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T29321hsView(View):
      
    def post(self,request):
         
         t29321h_data=JSONParser().parse(request)
         t29321h_serializer=T29321hSerializer(data=t29321h_data)
         if t29321h_serializer.is_valid():
             t29321h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t29321hs = T29321hs.objects.all()
         t29321h_serializer=T29321hSerializer(t29321hs,many=True)
         return JsonResponse(t29321h_serializer.data,safe=False)

    def put(self,request):
         t29321h_data=JSONParser().parse(request)
         t29321h=T29321hs.objects.get(id_temp_aire_min=t29321h_data['id_temp_aire_min'])
         t29321h_serializer=T1073161hSerializer(t29321h,data=t29321h_data)
         if t29321h_serializer.is_valid():
            t29321h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t29321h=T29321hs.objects.get(id_temp_aire_min=id)
        t29321h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class T29321hvalsView(View):
      
    def post(self,request):
         
         t29321hval_data=JSONParser().parse(request)
         t29321hval_serializer=T29321hvalSerializer(data=t29321hval_data)
         if t29321hval_serializer.is_valid():
             t29321hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t29321hvals = T29321hvals.objects.all()
         t29321hval_serializer=T29321hvalSerializer(t29321hvals,many=True)
         return JsonResponse(t29321hval_serializer.data,safe=False)

    def put(self,request):
         t29321hval_data=JSONParser().parse(request)
         t29321hval=T29321hvals.objects.get(id_temp_aire_min_val=t29321hval_data['id_temp_aire_min_val'])
         t29321hval_serializer=T1073161hSerializer(t29321hval,data=t29321hval_data)
         if t29321hval_serializer.is_valid():
            t29321hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t29321hval=T29321hvals.objects.get(id_temp_aire_min_val=id)
        t29321hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T303161hsView(View):
      
    def post(self,request):
         
         t303161h_data=JSONParser().parse(request)
         t303161h_serializer=T303161hSerializer(data=t303161h_data)
         if t303161h_serializer.is_valid():
             t303161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t303161hs = T303161hs.objects.all()
         t303161h_serializer=T303161hSerializer(t303161hs,many=True)
         return JsonResponse(t303161h_serializer.data,safe=False)

    def put(self,request):
         t303161h_data=JSONParser().parse(request)
         t303161h=T303161hs.objects.get(id_temp_agua_mar=t303161h_data['id_temp_agua_mar'])
         t303161h_serializer=T1073161hSerializer(t303161h,data=t303161h_data)
         if t303161h_serializer.is_valid():
            t303161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t303161h=T303161hs.objects.get(id_temp_agua_mar=id)
        t303161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class T303161hvalsView(View):
      
    def post(self,request):
         
         t303161hval_data=JSONParser().parse(request)
         t303161hval_serializer=T303161hvalSerializer(data=t303161hval_data)
         if t303161hval_serializer.is_valid():
             t303161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t303161hvals = T303161hvals.objects.all()
         t303161hval_serializer=T303161hvalSerializer(t303161hvals,many=True)
         return JsonResponse(t303161hval_serializer.data,safe=False)

    def put(self,request):
         t303161hval_data=JSONParser().parse(request)
         t303161hval=T303161hvals.objects.get(id_temp_agua_mar_val=t303161hval_data['id_temp_agua_mar_val'])
         t303161hval_serializer=T1073161hSerializer(t303161hval,data=t303161hval_data)
         if t303161hval_serializer.is_valid():
            t303161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t303161hval=T303161hvals.objects.get(id_temp_agua_mar_val=id)
        t303161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T42161hsView(View):
      
    def post(self,request):
         
         t42161h_data=JSONParser().parse(request)
         t42161h_serializer=T42161hSerializer(data=t42161h_data)
         if t42161h_serializer.is_valid():
             t42161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t42161hs = T42161hs.objects.all()
         t42161h_serializer=T42161hSerializer(t42161hs,many=True)
         return JsonResponse(t42161h_serializer.data,safe=False)

    def put(self,request):
         t42161h_data=JSONParser().parse(request)
         t42161h=T42161hs.objects.get(id_tiento_dir=t42161h_data['id_tiento_dir'])
         t42161h_serializer=T1073161hSerializer(t42161h,data=t42161h_data)
         if t42161h_serializer.is_valid():
            t42161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t42161h=T42161hs.objects.get(id_tiento_dir=id)
        t42161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class T42161hvalsView(View):
      
    def post(self,request):
         
         t42161hval_data=JSONParser().parse(request)
         t42161hval_serializer=T42161hvalSerializer(data=t42161hval_data)
         if t42161hval_serializer.is_valid():
             t42161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t42161hvals = T42161hvals.objects.all()
         t42161hval_serializer=T42161hvalSerializer(t42161hvals,many=True)
         return JsonResponse(t42161hval_serializer.data,safe=False)

    def put(self,request):
         t42161hval_data=JSONParser().parse(request)
         t42161hval=T42161hvals.objects.get(id_tiento_dir_val=t42161hval_data['id_tiento_dir_val'])
         t42161hval_serializer=T1073161hSerializer(t42161hval,data=t42161hval_data)
         if t42161hval_serializer.is_valid():
            t42161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t42161hval=T42161hvals.objects.get(id_tiento_dir_val=id)
        t42161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T557161hsView(View):
      
    def post(self,request):
         
         t557161h_data=JSONParser().parse(request)
         t557161h_serializer=T557161hSerializer(data=t557161h_data)
         if t557161h_serializer.is_valid():
             t557161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t557161hs = T557161hs.objects.all()
         t557161h_serializer=T557161hSerializer(t557161hs,many=True)
         return JsonResponse(t557161h_serializer.data,safe=False)

    def put(self,request):
         t557161h_data=JSONParser().parse(request)
         t557161h=T557161hs.objects.get(id_pres_red=t557161h_data['id_pres_red'])
         t557161h_serializer=T1073161hSerializer(t557161h,data=t557161h_data)
         if t557161h_serializer.is_valid():
            t557161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t557161h=T557161hs.objects.get(id_pres_red=id)
        t557161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T557161hvalsView(View):
      
    def post(self,request):
         
         t557161hval_data=JSONParser().parse(request)
         t557161hval_serializer=T557161hvalSerializer(data=t557161hval_data)
         if t557161hval_serializer.is_valid():
             t557161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t557161hvals = T557161hvals.objects.all()
         t557161hval_serializer=T557161hvalSerializer(t557161hvals,many=True)
         return JsonResponse(t557161hval_serializer.data,safe=False)

    def put(self,request):
         t557161hval_data=JSONParser().parse(request)
         t557161hval=T557161hvals.objects.get(id_pres_red_val=t557161hval_data['id_pres_red_val'])
         t557161hval_serializer=T1073161hSerializer(t557161hval,data=t557161hval_data)
         if t557161hval_serializer.is_valid():
            t557161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t557161hval=T557161hvals.objects.get(id_pres_red_val=id)
        t557161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T573161hsView(View):
      
    def post(self,request):
         
         t573161h_data=JSONParser().parse(request)
         t573161h_serializer=T573161hSerializer(data=t573161h_data)
         if t573161h_serializer.is_valid():
             t573161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t573161hs = T573161hs.objects.all()
         t573161h_serializer=T573161hSerializer(t573161hs,many=True)
         return JsonResponse(t573161h_serializer.data,safe=False)

    def put(self,request):
         t573161h_data=JSONParser().parse(request)
         t573161h=T573161hs.objects.get(id_term_seco=t573161h_data['id_term_seco'])
         t573161h_serializer=T1073161hSerializer(t573161h,data=t573161h_data)
         if t573161h_serializer.is_valid():
            t573161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t573161h=T573161hs.objects.get(id_term_seco=id)
        t573161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T573161hvalsView(View):
      
    def post(self,request):
         
         t573161hval_data=JSONParser().parse(request)
         t573161hval_serializer=T573161hvalSerializer(data=t573161hval_data)
         if t573161hval_serializer.is_valid():
             t573161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t573161hvals = T573161hvals.objects.all()
         t573161hval_serializer=T573161hvalSerializer(t573161hvals,many=True)
         return JsonResponse(t573161hval_serializer.data,safe=False)

    def put(self,request):
         t573161hval_data=JSONParser().parse(request)
         t573161hval=T573161hvals.objects.get(id_term_seco_val=t573161hval_data['id_term_seco_val'])
         t573161hval_serializer=T1073161hSerializer(t573161hval,data=t573161hval_data)
         if t573161hval_serializer.is_valid():
            t573161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t573161hval=T573161hvals.objects.get(id_term_seco_val=id)
        t573161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)   


class T583161hsView(View):
      
    def post(self,request):
         
         t583161h_data=JSONParser().parse(request)
         t583161h_serializer=T583161hSerializer(data=t583161h_data)
         if t583161h_serializer.is_valid():
             t583161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t583161hs = T583161hs.objects.all()
         t583161h_serializer=T583161hSerializer(t583161hs,many=True)
         return JsonResponse(t583161h_serializer.data,safe=False)

    def put(self,request):
         t583161h_data=JSONParser().parse(request)
         t583161h=T583161hs.objects.get(id_term_hmd=t583161h_data['id_term_hmd'])
         t583161h_serializer=T1073161hSerializer(t583161h,data=t583161h_data)
         if t583161h_serializer.is_valid():
            t583161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t583161h=T583161hs.objects.get(id_term_hmd=id)
        t583161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T583161hvalsView(View):
      
    def post(self,request):
         
         t583161hval_data=JSONParser().parse(request)
         t583161hval_serializer=T583161hvalSerializer(data=t583161hval_data)
         if t583161hval_serializer.is_valid():
             t583161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t583161hvals = T583161hvals.objects.all()
         t583161hval_serializer=T583161hvalSerializer(t583161hvals,many=True)
         return JsonResponse(t583161hval_serializer.data,safe=False)

    def put(self,request):
         t583161hval_data=JSONParser().parse(request)
         t583161hval=T583161hvals.objects.get(id_term_hmd_val=t583161hval_data['id_term_hmd_val'])
         t583161hval_serializer=T1073161hSerializer(t583161hval,data=t583161hval_data)
         if t583161hval_serializer.is_valid():
            t583161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t583161hval=T583161hvals.objects.get(id_term_hmd_val=id)
        t583161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T597161hsView(View):
      
    def post(self,request):
         
         t597161h_data=JSONParser().parse(request)
         t597161h_serializer=T597161hSerializer(data=t597161h_data)
         if t597161h_serializer.is_valid():
             t597161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t597161hs = T597161hs.objects.all()
         t597161h_serializer=T597161hSerializer(t597161hs,many=True)
         return JsonResponse(t597161h_serializer.data,safe=False)

    def put(self,request):
         t597161h_data=JSONParser().parse(request)
         t597161h=T597161hs.objects.get(id_tension_tapor=t597161h_data['id_tension_tapor'])
         t597161h_serializer=T1073161hSerializer(t597161h,data=t597161h_data)
         if t597161h_serializer.is_valid():
            t597161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t597161h=T597161hs.objects.get(id_tension_tapor=id)
        t597161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)    


class T597161hvalsView(View):
      
    def post(self,request):
         
         t597161hval_data=JSONParser().parse(request)
         t597161hval_serializer=T597161hvalSerializer(data=t597161hval_data)
         if t597161hval_serializer.is_valid():
             t597161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t597161hvals = T597161hvals.objects.all()
         t597161hval_serializer=T597161hvalSerializer(t597161hvals,many=True)
         return JsonResponse(t597161hval_serializer.data,safe=False)

    def put(self,request):
         t597161hval_data=JSONParser().parse(request)
         t597161hval=T597161hvals.objects.get(id_tension_tapor_val=t597161hval_data['id_tension_tapor_val'])
         t597161hval_serializer=T1073161hSerializer(t597161hval,data=t597161hval_data)
         if t597161hval_serializer.is_valid():
            t597161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t597161hval=T597161hvals.objects.get(id_tension_tapor_val=id)
        t597161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T603161hsView(View):
      
    def post(self,request):
         
         t603161h_data=JSONParser().parse(request)
         t603161h_serializer=T603161hSerializer(data=t603161h_data)
         if t603161h_serializer.is_valid():
             t603161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t603161hs = T603161hs.objects.all()
         t603161h_serializer=T603161hSerializer(t603161hs,many=True)
         return JsonResponse(t603161h_serializer.data,safe=False)

    def put(self,request):
         t603161h_data=JSONParser().parse(request)
         t603161h=T603161hs.objects.get(id_punto_rocio=t603161h_data['id_punto_rocio'])
         t603161h_serializer=T1073161hSerializer(t603161h,data=t603161h_data)
         if t603161h_serializer.is_valid():
            t603161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t603161h=T603161hs.objects.get(id_punto_rocio=id)
        t603161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class T603161hvalsView(View):
      
    def post(self,request):
         
         t603161hval_data=JSONParser().parse(request)
         t603161hval_serializer=T603161hvalSerializer(data=t603161hval_data)
         if t603161hval_serializer.is_valid():
             t603161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t603161hvals = T603161hvals.objects.all()
         t603161hval_serializer=T603161hvalSerializer(t603161hvals,many=True)
         return JsonResponse(t603161hval_serializer.data,safe=False)

    def put(self,request):
         t603161hval_data=JSONParser().parse(request)
         t603161hval=T603161hvals.objects.get(id_punto_rocio_val=t603161hval_data['id_punto_rocio_val'])
         t603161hval_serializer=T1073161hSerializer(t603161hval,data=t603161hval_data)
         if t603161hval_serializer.is_valid():
            t603161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t603161hval=T603161hvals.objects.get(id_punto_rocio_val=id)
        t603161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T614161hsView(View):
      
    def post(self,request):
         
         t614161h_data=JSONParser().parse(request)
         t614161h_serializer=T614161hSerializer(data=t614161h_data)
         if t614161h_serializer.is_valid():
             t614161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t614161hs = T614161hs.objects.all()
         t614161h_serializer=T614161hSerializer(t614161hs,many=True)
         return JsonResponse(t614161h_serializer.data,safe=False)

    def put(self,request):
         t614161h_data=JSONParser().parse(request)
         t614161h=T614161hs.objects.get(id_etapo=t614161h_data['id_etapo'])
         t614161h_serializer=T1073161hSerializer(t614161h,data=t614161h_data)
         if t614161h_serializer.is_valid():
            t614161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t614161h=T614161hs.objects.get(id_etapo=id)
        t614161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T614161hvalsView(View):
      
    def post(self,request):
         
         t614161hval_data=JSONParser().parse(request)
         t614161hval_serializer=T614161hvalSerializer(data=t614161hval_data)
         if t614161hval_serializer.is_valid():
             t614161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t614161hvals = T614161hvals.objects.all()
         t614161hval_serializer=T614161hvalSerializer(t614161hvals,many=True)
         return JsonResponse(t614161hval_serializer.data,safe=False)

    def put(self,request):
         t614161hval_data=JSONParser().parse(request)
         t614161hval=T614161hvals.objects.get(id_etapo_val=t614161hval_data['id_etapo_val'])
         t614161hval_serializer=T1073161hSerializer(t614161hval,data=t614161hval_data)
         if t614161hval_serializer.is_valid():
            t614161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t614161hval=T614161hvals.objects.get(id_etapo_val=id)
        t614161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False) 



class T644161hsView(View):
      
    def post(self,request):
         
         t644161h_data=JSONParser().parse(request)
         t644161h_serializer=T644161hSerializer(data=t644161h_data)
         if t644161h_serializer.is_valid():
             t644161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t644161hs = T644161hs.objects.all()
         t644161h_serializer=T644161hSerializer(t644161hs,many=True)
         return JsonResponse(t644161h_serializer.data,safe=False)

    def put(self,request):
         t644161h_data=JSONParser().parse(request)
         t644161h=T644161hs.objects.get(id_nube=t644161h_data['id_nube'])
         t644161h_serializer=T1073161hSerializer(t644161h,data=t644161h_data)
         if t644161h_serializer.is_valid():
            t644161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t644161h=T644161hs.objects.get(id_nube=id)
        t644161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T644161hvalsView(View):
      
    def post(self,request):
         
         t644161hval_data=JSONParser().parse(request)
         t644161hval_serializer=T644161hvalSerializer(data=t644161hval_data)
         if t644161hval_serializer.is_valid():
             t644161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t644161hvals = T644161hvals.objects.all()
         t644161hval_serializer=T644161hvalSerializer(t644161hvals,many=True)
         return JsonResponse(t644161hval_serializer.data,safe=False)

    def put(self,request):
         t644161hval_data=JSONParser().parse(request)
         t644161hval=T644161hvals.objects.get(id_nube_val=t644161hval_data['id_nube_val'])
         t644161hval_serializer=T1073161hSerializer(t644161hval,data=t644161hval_data)
         if t644161hval_serializer.is_valid():
            t644161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t644161hval=T644161hvals.objects.get(id_nube_val=id)
        t644161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T674161hsView(View):
      
    def post(self,request):
         
         t674161h_data=JSONParser().parse(request)
         t674161h_serializer=T674161hSerializer(data=t674161h_data)
         if t674161h_serializer.is_valid():
             t674161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t674161hs = T674161hs.objects.all()
         t674161h_serializer=T674161hSerializer(t674161hs,many=True)
         return JsonResponse(t674161h_serializer.data,safe=False)

    def put(self,request):
         t674161h_data=JSONParser().parse(request)
         t674161h=T674161hs.objects.get(id_nube=t674161h_data['id_nube'])
         t674161h_serializer=T1073161hSerializer(t674161h,data=t674161h_data)
         if t674161h_serializer.is_valid():
            t674161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t674161h=T674161hs.objects.get(id_nube=id)
        t674161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T674161hvalsView(View):
      
    def post(self,request):
         
         t674161hval_data=JSONParser().parse(request)
         t674161hval_serializer=T674161hvalSerializer(data=t674161hval_data)
         if t674161hval_serializer.is_valid():
             t674161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t674161hvals = T674161hvals.objects.all()
         t674161hval_serializer=T674161hvalSerializer(t674161hvals,many=True)
         return JsonResponse(t674161hval_serializer.data,safe=False)

    def put(self,request):
         t674161hval_data=JSONParser().parse(request)
         t674161hval=T674161hvals.objects.get(id_nube_val=t674161hval_data['id_nube_val'])
         t674161hval_serializer=T1073161hSerializer(t674161hval,data=t674161hval_data)
         if t674161hval_serializer.is_valid():
            t674161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t674161hval=T674161hvals.objects.get(id_nube_val=id)
        t674161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)    



class T704161hsView(View):
      
    def post(self,request):
         
         t704161h_data=JSONParser().parse(request)
         t704161h_serializer=T704161hSerializer(data=t704161h_data)
         if t704161h_serializer.is_valid():
             t704161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t704161hs = T704161hs.objects.all()
         t704161h_serializer=T704161hSerializer(t704161hs,many=True)
         return JsonResponse(t704161h_serializer.data,safe=False)

    def put(self,request):
         t704161h_data=JSONParser().parse(request)
         t704161h=T704161hs.objects.get(id_nube=t704161h_data['id_nube'])
         t704161h_serializer=T1073161hSerializer(t704161h,data=t704161h_data)
         if t704161h_serializer.is_valid():
            t704161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t704161h=T704161hs.objects.get(id_nube=id)
        t704161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T704161hvalsView(View):
      
    def post(self,request):
         
         t704161hval_data=JSONParser().parse(request)
         t704161hval_serializer=T704161hvalSerializer(data=t704161hval_data)
         if t704161hval_serializer.is_valid():
             t704161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t704161hvals = T704161hvals.objects.all()
         t704161hval_serializer=T704161hvalSerializer(t704161hvals,many=True)
         return JsonResponse(t704161hval_serializer.data,safe=False)

    def put(self,request):
         t704161hval_data=JSONParser().parse(request)
         t704161hval=T704161hvals.objects.get(id_nube_val=t704161hval_data['id_nube_val'])
         t704161hval_serializer=T1073161hSerializer(t704161hval,data=t704161hval_data)
         if t704161hval_serializer.is_valid():
            t704161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t704161hval=T704161hvals.objects.get(id_nube_val=id)
        t704161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class T7229161hsView(View):
      
    def post(self,request):
         
         t7229161h_data=JSONParser().parse(request)
         t7229161h_serializer=T7229161hSerializer(data=t7229161h_data)
         if t7229161h_serializer.is_valid():
             t7229161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t7229161hs = T7229161hs.objects.all()
         t7229161h_serializer=T7229161hSerializer(t7229161hs,many=True)
         return JsonResponse(t7229161h_serializer.data,safe=False)

    def put(self,request):
         t7229161h_data=JSONParser().parse(request)
         t7229161h=T7229161hs.objects.get(id_tisibilidad_hor=t7229161h_data['id_tisibilidad_hor'])
         t7229161h_serializer=T1073161hSerializer(t7229161h,data=t7229161h_data)
         if t7229161h_serializer.is_valid():
            t7229161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t7229161h=T7229161hs.objects.get(id_tisibilidad_hor=id)
        t7229161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  



class T7229161hvalsView(View):
      
    def post(self,request):
         
         t7229161hval_data=JSONParser().parse(request)
         t7229161hval_serializer=T7229161hvalSerializer(data=t7229161hval_data)
         if t7229161hval_serializer.is_valid():
             t7229161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t7229161hvals = T7229161hvals.objects.all()
         t7229161hval_serializer=T7229161hvalSerializer(t7229161hvals,many=True)
         return JsonResponse(t7229161hval_serializer.data,safe=False)

    def put(self,request):
         t7229161hval_data=JSONParser().parse(request)
         t7229161hval=T7229161hvals.objects.get(id_tisibilidad_hor_val=t7229161hval_data['id_tisibilidad_hor_val'])
         t7229161hval_serializer=T1073161hSerializer(t7229161hval,data=t7229161hval_data)
         if t7229161hval_serializer.is_valid():
            t7229161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t7229161hval=T7229161hvals.objects.get(id_tisibilidad_hor_val=id)
        t7229161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class T7514161hsView(View):
      
    def post(self,request):
         
         t7514161h_data=JSONParser().parse(request)
         t7514161h_serializer=T7514161hSerializer(data=t7514161h_data)
         if t7514161h_serializer.is_valid():
             t7514161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t7514161hs = T7514161hs.objects.all()
         t7514161h_serializer=T7514161hSerializer(t7514161hs,many=True)
         return JsonResponse(t7514161h_serializer.data,safe=False)

    def put(self,request):
         t7514161h_data=JSONParser().parse(request)
         t7514161h=T7514161hs.objects.get(id_reduc_tanque=t7514161h_data['id_reduc_tanque'])
         t7514161h_serializer=T1073161hSerializer(t7514161h,data=t7514161h_data)
         if t7514161h_serializer.is_valid():
            t7514161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t7514161h=T7514161hs.objects.get(id_reduc_tanque=id)
        t7514161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class T7514161hvalsView(View):
      
    def post(self,request):
         
         t7514161hval_data=JSONParser().parse(request)
         t7514161hval_serializer=T7514161hvalSerializer(data=t7514161hval_data)
         if t7514161hval_serializer.is_valid():
             t7514161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t7514161hvals = T7514161hvals.objects.all()
         t7514161hval_serializer=T7514161hvalSerializer(t7514161hvals,many=True)
         return JsonResponse(t7514161hval_serializer.data,safe=False)

    def put(self,request):
         t7514161hval_data=JSONParser().parse(request)
         t7514161hval=T7514161hvals.objects.get(id_reduc_tanque_val=t7514161hval_data['id_reduc_tanque_val'])
         t7514161hval_serializer=T1073161hSerializer(t7514161hval,data=t7514161hval_data)
         if t7514161hval_serializer.is_valid():
            t7514161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t7514161hval=T7514161hvals.objects.get(id_reduc_tanque_val=id)
        t7514161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class T765161hsView(View):
      
    def post(self,request):
         
         t765161h_data=JSONParser().parse(request)
         t765161h_serializer=T765161hSerializer(data=t765161h_data)
         if t765161h_serializer.is_valid():
             t765161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t765161hs = T765161hs.objects.all()
         t765161h_serializer=T765161hSerializer(t765161hs,many=True)
         return JsonResponse(t765161h_serializer.data,safe=False)

    def put(self,request):
         t765161h_data=JSONParser().parse(request)
         t765161h=T765161hs.objects.get(id_agua_sacada=t765161h_data['id_agua_sacada'])
         t765161h_serializer=T1073161hSerializer(t765161h,data=t765161h_data)
         if t765161h_serializer.is_valid():
            t765161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t765161h=T765161hs.objects.get(id_agua_sacada=id)
        t765161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class T765161hvalsView(View):
      
    def post(self,request):
         
         t765161hval_data=JSONParser().parse(request)
         t765161hval_serializer=T765161hvalSerializer(data=t765161hval_data)
         if t765161hval_serializer.is_valid():
             t765161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t765161hvals = T765161hvals.objects.all()
         t765161hval_serializer=T765161hvalSerializer(t765161hvals,many=True)
         return JsonResponse(t765161hval_serializer.data,safe=False)

    def put(self,request):
         t765161hval_data=JSONParser().parse(request)
         t765161hval=T765161hvals.objects.get(id_agua_sacada_val=t765161hval_data['id_agua_sacada_val'])
         t765161hval_serializer=T1073161hSerializer(t765161hval,data=t765161hval_data)
         if t765161hval_serializer.is_valid():
            t765161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t765161hval=T765161hvals.objects.get(id_agua_sacada_val=id)
        t765161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class T775161hsView(View):
      
    def post(self,request):
         
         t775161h_data=JSONParser().parse(request)
         t775161h_serializer=T775161hSerializer(data=t775161h_data)
         if t775161h_serializer.is_valid():
             t775161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t775161hs = T775161hs.objects.all()
         t775161h_serializer=T775161hSerializer(t775161hs,many=True)
         return JsonResponse(t775161h_serializer.data,safe=False)

    def put(self,request):
         t775161h_data=JSONParser().parse(request)
         t775161h=T775161hs.objects.get(id_agua_aniadida=t775161h_data['id_agua_aniadida'])
         t775161h_serializer=T1073161hSerializer(t775161h,data=t775161h_data)
         if t775161h_serializer.is_valid():
            t775161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t775161h=T775161hs.objects.get(id_agua_aniadida=id)
        t775161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  
        

class T775161hvalsView(View):
      
    def post(self,request):
         
         t775161hval_data=JSONParser().parse(request)
         t775161hval_serializer=T775161hvalSerializer(data=t775161hval_data)
         if t775161hval_serializer.is_valid():
             t775161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t775161hvals = T775161hvals.objects.all()
         t775161hval_serializer=T775161hvalSerializer(t775161hvals,many=True)
         return JsonResponse(t775161hval_serializer.data,safe=False)

    def put(self,request):
         t775161hval_data=JSONParser().parse(request)
         t775161hval=T775161hvals.objects.get(id_agua_aniadida_val=t775161hval_data['id_agua_aniadida_val'])
         t775161hval_serializer=T1073161hSerializer(t775161hval,data=t775161hval_data)
         if t775161hval_serializer.is_valid():
            t775161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t775161hval=T775161hvals.objects.get(id_agua_aniadida_val=id)
        t775161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class T91161hsView(View):
      
    def post(self,request):
         
         t91161h_data=JSONParser().parse(request)
         t91161h_serializer=T91161hSerializer(data=t91161h_data)
         if t91161h_serializer.is_valid():
             t91161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t91161hs = T91161hs.objects.all()
         t91161h_serializer=T91161hSerializer(t91161hs,many=True)
         return JsonResponse(t91161h_serializer.data,safe=False)

    def put(self,request):
         t91161h_data=JSONParser().parse(request)
         t91161h=T91161hs.objects.get(id_humedad_rltta=t91161h_data['id_humedad_rltta'])
         t91161h_serializer=T1073161hSerializer(t91161h,data=t91161h_data)
         if t91161h_serializer.is_valid():
            t91161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t91161h=T91161hs.objects.get(id_humedad_rltta=id)
        t91161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  



class T91161hvalsView(View):
      
    def post(self,request):
         
         t91161hval_data=JSONParser().parse(request)
         t91161hval_serializer=T91161hvalSerializer(data=t91161hval_data)
         if t91161hval_serializer.is_valid():
             t91161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         t91161hvals = T91161hvals.objects.all()
         t91161hval_serializer=T91161hvalSerializer(t91161hvals,many=True)
         return JsonResponse(t91161hval_serializer.data,safe=False)

    def put(self,request):
         t91161hval_data=JSONParser().parse(request)
         t91161hval=T91161hvals.objects.get(id_humedad_rltta_val=t91161hval_data['id_humedad_rltta_val'])
         t91161hval_serializer=T1073161hSerializer(t91161hval,data=t91161hval_data)
         if t91161hval_serializer.is_valid():
            t91161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        t91161hval=T91161hvals.objects.get(id_humedad_rltta_val=id)
        t91161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  

class CalView(View):

    def calevapo():
         

        return JsonResponse("hola")


  


   


 


     



  