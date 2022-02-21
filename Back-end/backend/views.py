from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.relations import method_overridden
from rest_framework.utils import json
from django.views.generic import View
from backend.models import *
from backend.serializers import *
from django.http import HttpResponse

class V1073161hsApi(View):
      
    def post(self,request):
         v1073161h_data=JSONParser().parse(request)
         v1073161h_serializer=V1073161hSerializer(data=v1073161h_data)
         if v1073161h_serializer.is_valid():
             v1073161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1073161hs = V1073161hs.objects.all()
         v1073161h_serializer=V1073161hSerializer(v1073161hs,many=True)
         return JsonResponse(v1073161h_serializer.data,safe=False)

    def put(self,request):
         v1073161h_data=JSONParser().parse(request)
         v1073161h=V1073161hs.objects.get(id_temp_int_baro=v1073161h_data['id_temp_int_baro'])
         v1073161h_serializer=V1073161hSerializer(v1073161h,data=v1073161h_data)
         if v1073161h_serializer.is_valid():
            v1073161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1073161h=V1073161hs.objects.get(id_temp_int_baro=id)
        v1073161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)
 
class V1073161hvalsApi(View):
      
    def post(self,request):
         v1073161hval_data=JSONParser().parse(request)
         v1073161hval_serializer=V1073161hvalSerializer(data=v1073161hval_data)
         if v1073161hval_serializer.is_valid():
             v1073161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1073161hvals = V1073161hvals.objects.all()
         v1073161hval_serializer=V1073161hvalSerializer(v1073161hvals,many=True)
         return JsonResponse(v1073161hval_serializer.data,safe=False)

    def put(self,request):
         v1073161hval_data=JSONParser().parse(request)
         v1073161hval=V1073161hvals.objects.get(id_temp_int_baro_val=v1073161hval_data['id_temp_int_baro_val'])
         v1073161hval_serializer=V1073161hSerializer(v1073161hval,data=v1073161hval_data)
         if v1073161hval_serializer.is_valid():
            v1073161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1073161hval=V1073161hvals.objects.get(id_temp_int_baro_val=id)
        v1073161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)


class V1087161hsApi(View):
      
    def post(self,request):
         v1087161h_data=JSONParser().parse(request)
         v1087161h_serializer=V1087161hSerializer(data=v1087161h_data)
         if v1087161h_serializer.is_valid():
             v1087161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1087161hs = V1087161hs.objects.all()
         v1087161h_serializer=V1087161hSerializer(v1087161hs,many=True)
         return JsonResponse(v1087161h_serializer.data,safe=False)

    def put(self,request):
         v1087161h_data=JSONParser().parse(request)
         v1087161h=V1087161hs.objects.get(id_pres_corre=v1087161h_data['id_temp_int_baro_val'])
         v1087161h_serializer=V1087161hSerializer(v1087161h,data=v1087161h_data)
         if v1087161h_serializer.is_valid():
            v1087161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1087161h=V1087161hs.objects.get(id_pres_corre=id)
        v1087161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)


class V1087161hvalsApi(View):
      
    def post(self,request):
         v1087161hval_data=JSONParser().parse(request)
         v1087161hval_serializer=V1087161hvalSerializer(data=v1087161hval_data)
         if v1087161hval_serializer.is_valid():
             v1087161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1087161hvals = V1087161hvals.objects.all()
         v1087161hval_serializer=V1087161hvalSerializer(v1087161hvals,many=True)
         return JsonResponse(v1087161hval_serializer.data,safe=False)

    def put(self,request):
         v1087161hval_data=JSONParser().parse(request)
         v1087161hval=V1087161hvals.objects.get(id_pres_corre_val=v1087161hval_data['id_temp_int_baro_val'])
         v1087161hval_serializer=V1073161hSerializer(v1087161hval,data=v1087161hval_data)
         if v1087161hval_serializer.is_valid():
            v1087161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1087161hval=V1087161hvals.objects.get(id_pres_corre_val=id)
        v1087161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False) 

class V1097161hsApi(View):
      
    def post(self,request):
         
         v1097161h_data=JSONParser().parse(request)
         v1097161h_serializer=V1097161hSerializer(data=v1097161h_data)
         if v1097161h_serializer.is_valid():
             v1097161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1097161hs = V1097161hs.objects.all()
         v1097161h_serializer=V1097161hSerializer(v1097161hs,many=True)
         return JsonResponse(v1097161h_serializer.data,safe=False)

    def put(self,request):
         v1097161h_data=JSONParser().parse(request)
         v1097161h=V1097161hs.objects.get(id_pres_conv=v1097161h_data['id_pres_conv'])
         v1097161h_serializer=V1073161hSerializer(v1097161h,data=v1097161h_data)
         if v1097161h_serializer.is_valid():
            v1097161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1097161h=V1097161hs.objects.get(id_pres_conv=id)
        v1097161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)        


class V1097161hvalsApi(View):
      
    def post(self,request):
         
         v1097161hval_data=JSONParser().parse(request)
         v1097161hval_serializer=V1097161hvalSerializer(data=v1097161hval_data)
         if v1097161hval_serializer.is_valid():
             v1097161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1097161hvals = V1097161hvals.objects.all()
         v1097161hval_serializer=V1097161hvalSerializer(v1097161hvals,many=True)
         return JsonResponse(v1097161hval_serializer.data,safe=False)

    def put(self,request):
         v1097161hval_data=JSONParser().parse(request)
         v1097161hval=V1097161hvals.objects.get(id_pres_conv_val=v1097161hval_data['id_pres_conv_val'])
         v1097161hval_serializer=V1073161hSerializer(v1097161hval,data=v1097161hval_data)
         if v1097161hval_serializer.is_valid():
            v1097161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1097161hval=V1097161hvals.objects.get(id_pres_conv_val=id)
        v1097161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)      


class V1263011hsApi(View):
      
    def post(self,request):
         
         v1263011h_data=JSONParser().parse(request)
         v1263011h_serializer=V1263011hSerializer(data=v1263011h_data)
         if v1263011h_serializer.is_valid():
             v1263011h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1263011hs = V1263011hs.objects.all()
         v1263011h_serializer=V1263011hSerializer(v1263011hs,many=True)
         return JsonResponse(v1263011h_serializer.data,safe=False)

    def put(self,request):
         v1263011h_data=JSONParser().parse(request)
         v1263011h=V1263011hs.objects.get(id_caudal_max_hor=v1263011h_data['id_caudal_max_hor'])
         v1263011h_serializer=V1073161hSerializer(v1263011h,data=v1263011h_data)
         if v1263011h_serializer.is_valid():
            v1263011h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1263011h=V1263011hs.objects.get(id_caudal_max_hor=id)
        v1263011h.delete()
        return JsonResponse("Deleted Successfully",safe=False)      


class V1263011hvalsApi(View):
      
    def post(self,request):
         
         v1263011hval_data=JSONParser().parse(request)
         v1263011hval_serializer=V1263011hvalSerializer(data=v1263011hval_data)
         if v1263011hval_serializer.is_valid():
             v1263011hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1263011hvals = V1263011hvals.objects.all()
         v1263011hval_serializer=V1263011hvalSerializer(v1263011hvals,many=True)
         return JsonResponse(v1263011hval_serializer.data,safe=False)

    def put(self,request):
         v1263011hval_data=JSONParser().parse(request)
         v1263011hval=V1263011hvals.objects.get(id_caudal_max_hor_val=v1263011hval_data['id_caudal_max_hor_val'])
         v1263011hval_serializer=V1073161hSerializer(v1263011hval,data=v1263011hval_data)
         if v1263011hval_serializer.is_valid():
            v1263011hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1263011hval=V1263011hvals.objects.get(id_caudal_max_hor_val=id)
        v1263011hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V12630161hsApi(View):
      
    def post(self,request):
         
         v12630161h_data=JSONParser().parse(request)
         v12630161h_serializer=V12630161hSerializer(data=v12630161h_data)
         if v12630161h_serializer.is_valid():
             v12630161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v12630161hs = V12630161hs.objects.all()
         v12630161h_serializer=V12630161hSerializer(v12630161hs,many=True)
         return JsonResponse(v12630161h_serializer.data,safe=False)

    def put(self,request):
         v12630161h_data=JSONParser().parse(request)
         v12630161h=V12630161hs.objects.get(id_caudal_ins_hor=v12630161h_data['id_caudal_ins_hor'])
         v12630161h_serializer=V1073161hSerializer(v12630161h,data=v12630161h_data)
         if v12630161h_serializer.is_valid():
            v12630161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v12630161h=V12630161hs.objects.get(id_caudal_ins_hor=id)
        v12630161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class V12630161hvalsApi(View):
      
    def post(self,request):
         
         v12630161hval_data=JSONParser().parse(request)
         v12630161hval_serializer=V12630161hvalSerializer(data=v12630161hval_data)
         if v12630161hval_serializer.is_valid():
             v12630161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v12630161hvals = V12630161hvals.objects.all()
         v12630161hval_serializer=V12630161hvalSerializer(v12630161hvals,many=True)
         return JsonResponse(v12630161hval_serializer.data,safe=False)

    def put(self,request):
         v12630161hval_data=JSONParser().parse(request)
         v12630161hval=V12630161hvals.objects.get(id_caudal_ins_hor_val=v12630161hval_data['id_caudal_ins_hor_val'])
         v12630161hval_serializer=V1073161hSerializer(v12630161hval,data=v12630161hval_data)
         if v12630161hval_serializer.is_valid():
            v12630161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v12630161hval=V12630161hvals.objects.get(id_caudal_ins_hor_val=id)
        v12630161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False) 


class V1263021hsApi(View):
      
    def post(self,request):
         
         v1263021h_data=JSONParser().parse(request)
         v1263021h_serializer=V1263021hSerializer(data=v1263021h_data)
         if v1263021h_serializer.is_valid():
             v1263021h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1263021hs = V1263021hs.objects.all()
         v1263021h_serializer=V1263021hSerializer(v1263021hs,many=True)
         return JsonResponse(v1263021h_serializer.data,safe=False)

    def put(self,request):
         v1263021h_data=JSONParser().parse(request)
         v1263021h=V1263021hs.objects.get(id_caudal_min_hor=v1263021h_data['id_caudal_min_hor'])
         v1263021h_serializer=V1073161hSerializer(v1263021h,data=v1263021h_data)
         if v1263021h_serializer.is_valid():
            v1263021h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1263021h=V1263021hs.objects.get(id_caudal_min_hor=id)
        v1263021h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     



class V1263021hvalsApi(View):
      
    def post(self,request):
         
         v1263021hval_data=JSONParser().parse(request)
         v1263021hval_serializer=V1263021hvalSerializer(data=v1263021hval_data)
         if v1263021hval_serializer.is_valid():
             v1263021hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1263021hvals = V1263021hvals.objects.all()
         v1263021hval_serializer=V1263021hvalSerializer(v1263021hvals,many=True)
         return JsonResponse(v1263021hval_serializer.data,safe=False)

    def put(self,request):
         v1263021hval_data=JSONParser().parse(request)
         v1263021hval=V1263021hvals.objects.get(id_caudal_min_hor_val=v1263021hval_data['id_caudal_min_hor_val'])
         v1263021hval_serializer=V1073161hSerializer(v1263021hval,data=v1263021hval_data)
         if v1263021hval_serializer.is_valid():
            v1263021hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1263021hval=V1263021hvals.objects.get(id_caudal_min_hor_val=id)
        v1263021hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V1263041hsApi(View):
      
    def post(self,request):
         
         v1263041h_data=JSONParser().parse(request)
         v1263041h_serializer=V1263041hSerializer(data=v1263041h_data)
         if v1263041h_serializer.is_valid():
             v1263041h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1263041hs = V1263041hs.objects.all()
         v1263041h_serializer=V1263041hSerializer(v1263041hs,many=True)
         return JsonResponse(v1263041h_serializer.data,safe=False)

    def put(self,request):
         v1263041h_data=JSONParser().parse(request)
         v1263041h=V1263041hs.objects.get(id_caudal_prom_hor=v1263041h_data['id_caudal_prom_hor'])
         v1263041h_serializer=V1073161hSerializer(v1263041h,data=v1263041h_data)
         if v1263041h_serializer.is_valid():
            v1263041h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1263041h=V1263041hs.objects.get(id_caudal_prom_hor=id)
        v1263041h.delete()
        return JsonResponse("Deleted Successfully",safe=False)


class V1263041hvalsApi(View):
      
    def post(self,request):
         
         v1263041hval_data=JSONParser().parse(request)
         v1263041hval_serializer=V1263041hvalSerializer(data=v1263041hval_data)
         if v1263041hval_serializer.is_valid():
             v1263041hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1263041hvals = V1263041hvals.objects.all()
         v1263041hval_serializer=V1263041hvalSerializer(v1263041hvals,many=True)
         return JsonResponse(v1263041hval_serializer.data,safe=False)

    def put(self,request):
         v1263041hval_data=JSONParser().parse(request)
         v1263041hval=V1263041hvals.objects.get(id_caudal_prom_hor_val=v1263041hval_data['id_caudal_prom_hor_val'])
         v1263041hval_serializer=V1073161hSerializer(v1263041hval,data=v1263041hval_data)
         if v1263041hval_serializer.is_valid():
            v1263041hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1263041hval=V1263041hvals.objects.get(id_caudal_prom_hor_val=id)
        v1263041hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  



class V141011hsApi(View):
      
    def post(self,request):
         
         v141011h_data=JSONParser().parse(request)
         v141011h_serializer=V141011hSerializer(data=v141011h_data)
         if v141011h_serializer.is_valid():
             v141011h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v141011hs = V141011hs.objects.all()
         v141011h_serializer=V141011hSerializer(v141011hs,many=True)
         return JsonResponse(v141011h_serializer.data,safe=False)

    def put(self,request):
         v141011h_data=JSONParser().parse(request)
         v141011h=V141011hs.objects.get(id_nivelagua_max_hor=v141011h_data['id_nivelagua_max_hor'])
         v141011h_serializer=V1073161hSerializer(v141011h,data=v141011h_data)
         if v141011h_serializer.is_valid():
            v141011h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v141011h=V141011hs.objects.get(id_nivelagua_max_hor=id)
        v141011h.delete()
        return JsonResponse("Deleted Successfully",safe=False)          




class V141011hvalsApi(View):
      
    def post(self,request):
         
         v141011hval_data=JSONParser().parse(request)
         v141011hval_serializer=V141011hvalSerializer(data=v141011hval_data)
         if v141011hval_serializer.is_valid():
             v141011hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v141011hvals = V141011hvals.objects.all()
         v141011hval_serializer=V141011hvalSerializer(v141011hvals,many=True)
         return JsonResponse(v141011hval_serializer.data,safe=False)

    def put(self,request):
         v141011hval_data=JSONParser().parse(request)
         v141011hval=V141011hvals.objects.get(id_nivelagua_max_hor_val=v141011hval_data['id_nivelagua_max_hor_val'])
         v141011hval_serializer=V1073161hSerializer(v141011hval,data=v141011hval_data)
         if v141011hval_serializer.is_valid():
            v141011hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v141011hval=V141011hvals.objects.get(id_nivelagua_max_hor_val=id)
        v141011hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V1410161hsApi(View):
      
    def post(self,request):
         
         v1410161h_data=JSONParser().parse(request)
         v1410161h_serializer=V1410161hSerializer(data=v1410161h_data)
         if v1410161h_serializer.is_valid():
             v1410161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1410161hs = V1410161hs.objects.all()
         v1410161h_serializer=V1410161hSerializer(v1410161hs,many=True)
         return JsonResponse(v1410161h_serializer.data,safe=False)

    def put(self,request):
         v1410161h_data=JSONParser().parse(request)
         v1410161h=V1410161hs.objects.get(id_nivelagua_ins_hor=v1410161h_data['id_nivelagua_ins_hor'])
         v1410161h_serializer=V1073161hSerializer(v1410161h,data=v1410161h_data)
         if v1410161h_serializer.is_valid():
            v1410161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1410161h=V1410161hs.objects.get(id_nivelagua_ins_hor=id)
        v1410161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V1410161hvalsApi(View):
      
    def post(self,request):
         
         v1410161hval_data=JSONParser().parse(request)
         v1410161hval_serializer=V1410161hvalSerializer(data=v1410161hval_data)
         if v1410161hval_serializer.is_valid():
             v1410161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1410161hvals = V1410161hvals.objects.all()
         v1410161hval_serializer=V1410161hvalSerializer(v1410161hvals,many=True)
         return JsonResponse(v1410161hval_serializer.data,safe=False)

    def put(self,request):
         v1410161hval_data=JSONParser().parse(request)
         v1410161hval=V1410161hvals.objects.get(id_nivelagua_ins_hor_val=v1410161hval_data['id_nivelagua_ins_hor_val'])
         v1410161hval_serializer=V1073161hSerializer(v1410161hval,data=v1410161hval_data)
         if v1410161hval_serializer.is_valid():
            v1410161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1410161hval=V1410161hvals.objects.get(id_nivelagua_ins_hor_val=id)
        v1410161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V141021hsApi(View):
      
    def post(self,request):
         
         v141021h_data=JSONParser().parse(request)
         v141021h_serializer=V141021hSerializer(data=v141021h_data)
         if v141021h_serializer.is_valid():
             v141021h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v141021hs = V141021hs.objects.all()
         v141021h_serializer=V141021hSerializer(v141021hs,many=True)
         return JsonResponse(v141021h_serializer.data,safe=False)

    def put(self,request):
         v141021h_data=JSONParser().parse(request)
         v141021h=V141021hs.objects.get(id_nivelagua_min_hor=v141021h_data['id_nivelagua_min_hor'])
         v141021h_serializer=V1073161hSerializer(v141021h,data=v141021h_data)
         if v141021h_serializer.is_valid():
            v141021h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v141021h=V141021hs.objects.get(id_nivelagua_min_hor=id)
        v141021h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V141021hvalsApi(View):
      
    def post(self,request):
         
         v141021hval_data=JSONParser().parse(request)
         v141021hval_serializer=V141021hvalSerializer(data=v141021hval_data)
         if v141021hval_serializer.is_valid():
             v141021hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v141021hvals = V141021hvals.objects.all()
         v141021hval_serializer=V141021hvalSerializer(v141021hvals,many=True)
         return JsonResponse(v141021hval_serializer.data,safe=False)

    def put(self,request):
         v141021hval_data=JSONParser().parse(request)
         v141021hval=V141021hvals.objects.get(id_nivelagua_min_hor_val=v141021hval_data['id_nivelagua_min_hor_val'])
         v141021hval_serializer=V1073161hSerializer(v141021hval,data=v141021hval_data)
         if v141021hval_serializer.is_valid():
            v141021hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v141021hval=V141021hvals.objects.get(id_nivelagua_min_hor_val=id)
        v141021hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     



class V141041hsApi(View):
      
    def post(self,request):
         
         v141041h_data=JSONParser().parse(request)
         v141041h_serializer=V141041hSerializer(data=v141041h_data)
         if v141041h_serializer.is_valid():
             v141041h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v141041hs = V141041hs.objects.all()
         v141041h_serializer=V141041hSerializer(v141041hs,many=True)
         return JsonResponse(v141041h_serializer.data,safe=False)

    def put(self,request):
         v141041h_data=JSONParser().parse(request)
         v141041h=V141041hs.objects.get(id_nivelagua_prom_hor=v141041h_data['id_nivelagua_prom_hor'])
         v141041h_serializer=V1073161hSerializer(v141041h,data=v141041h_data)
         if v141041h_serializer.is_valid():
            v141041h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v141041h=V141041hs.objects.get(id_nivelagua_prom_hor=id)
        v141041h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class V141041hvalsApi(View):
      
    def post(self,request):
         
         v141041hval_data=JSONParser().parse(request)
         v141041hval_serializer=V141041hvalSerializer(data=v141041hval_data)
         if v141041hval_serializer.is_valid():
             v141041hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v141041hvals = V141041hvals.objects.all()
         v141041hval_serializer=V141041hvalSerializer(v141041hvals,many=True)
         return JsonResponse(v141041hval_serializer.data,safe=False)

    def put(self,request):
         v141041hval_data=JSONParser().parse(request)
         v141041hval=V141041hvals.objects.get(id_nivelagua_prom_hor_val=v141041hval_data['id_nivelagua_prom_hor_val'])
         v141041hval_serializer=V1073161hSerializer(v141041hval,data=v141041hval_data)
         if v141041hval_serializer.is_valid():
            v141041hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v141041hval=V141041hvals.objects.get(id_nivelagua_prom_hor_val=id)
        v141041hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)   


class V1714161hsApi(View):
      
    def post(self,request):
         
         v1714161h_data=JSONParser().parse(request)
         v1714161h_serializer=V1714161hSerializer(data=v1714161h_data)
         if v1714161h_serializer.is_valid():
             v1714161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1714161hs = V1714161hs.objects.all()
         v1714161h_serializer=V1714161hSerializer(v1714161hs,many=True)
         return JsonResponse(v1714161h_serializer.data,safe=False)

    def put(self,request):
         v1714161h_data=JSONParser().parse(request)
         v1714161h=V1714161hs.objects.get(id_prec_1h=v1714161h_data['id_prec_1h'])
         v1714161h_serializer=V1073161hSerializer(v1714161h,data=v1714161h_data)
         if v1714161h_serializer.is_valid():
            v1714161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1714161h=V1714161hs.objects.get(id_prec_1h=id)
        v1714161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)       


class V1714161hvalsApi(View):
      
    def post(self,request):
         
         v1714161hval_data=JSONParser().parse(request)
         v1714161hval_serializer=V1714161hvalSerializer(data=v1714161hval_data)
         if v1714161hval_serializer.is_valid():
             v1714161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v1714161hvals = V1714161hvals.objects.all()
         v1714161hval_serializer=V1714161hvalSerializer(v1714161hvals,many=True)
         return JsonResponse(v1714161hval_serializer.data,safe=False)

    def put(self,request):
         v1714161hval_data=JSONParser().parse(request)
         v1714161hval=V1714161hvals.objects.get(id_prec_1h_val=v1714161hval_data['id_prec_1h_val'])
         v1714161hval_serializer=V1073161hSerializer(v1714161hval,data=v1714161hval_data)
         if v1714161hval_serializer.is_valid():
            v1714161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v1714161hval=V1714161hvals.objects.get(id_prec_1h_val=id)
        v1714161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)   


class V171481hsApi(View):
      
    def post(self,request):
         
         v171481h_data=JSONParser().parse(request)
         v171481h_serializer=V171481hSerializer(data=v171481h_data)
         if v171481h_serializer.is_valid():
             v171481h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v171481hs = V171481hs.objects.all()
         v171481h_serializer=V171481hSerializer(v171481hs,many=True)
         return JsonResponse(v171481h_serializer.data,safe=False)

    def put(self,request):
         v171481h_data=JSONParser().parse(request)
         v171481h=V171481hs.objects.get(id_prec=v171481h_data['id_prec'])
         v171481h_serializer=V1073161hSerializer(v171481h,data=v171481h_data)
         if v171481h_serializer.is_valid():
            v171481h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v171481h=V171481hs.objects.get(id_prec=id)
        v171481h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V171481hvalsApi(View):
      
    def post(self,request):
         
         v171481hval_data=JSONParser().parse(request)
         v171481hval_serializer=V171481hvalSerializer(data=v171481hval_data)
         if v171481hval_serializer.is_valid():
             v171481hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v171481hvals = V171481hvals.objects.all()
         v171481hval_serializer=V171481hvalSerializer(v171481hvals,many=True)
         return JsonResponse(v171481hval_serializer.data,safe=False)

    def put(self,request):
         v171481hval_data=JSONParser().parse(request)
         v171481hval=V171481hvals.objects.get(id_prec_val=v171481hval_data['id_prec_val'])
         v171481hval_serializer=V1073161hSerializer(v171481hval,data=v171481hval_data)
         if v171481hval_serializer.is_valid():
            v171481hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v171481hval=V171481hvals.objects.get(id_prec_val=id)
        v171481hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V187161hsApi(View):
      
    def post(self,request):
         
         v187161h_data=JSONParser().parse(request)
         v187161h_serializer=V187161hSerializer(data=v187161h_data)
         if v187161h_serializer.is_valid():
             v187161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v187161hs = V187161hs.objects.all()
         v187161h_serializer=V187161hSerializer(v187161hs,many=True)
         return JsonResponse(v187161h_serializer.data,safe=False)

    def put(self,request):
         v187161h_data=JSONParser().parse(request)
         v187161h=V187161hs.objects.get(id_presion=v187161h_data['id_presion'])
         v187161h_serializer=V1073161hSerializer(v187161h,data=v187161h_data)
         if v187161h_serializer.is_valid():
            v187161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v187161h=V187161hs.objects.get(id_presion=id)
        v187161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V187161hvalsApi(View):
      
    def post(self,request):
         
         v187161hval_data=JSONParser().parse(request)
         v187161hval_serializer=V187161hvalSerializer(data=v187161hval_data)
         if v187161hval_serializer.is_valid():
             v187161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v187161hvals = V187161hvals.objects.all()
         v187161hval_serializer=V187161hvalSerializer(v187161hvals,many=True)
         return JsonResponse(v187161hval_serializer.data,safe=False)

    def put(self,request):
         v187161hval_data=JSONParser().parse(request)
         v187161hval=V187161hvals.objects.get(id_presion_val=v187161hval_data['id_presion_val'])
         v187161hval_serializer=V1073161hSerializer(v187161hval,data=v187161hval_data)
         if v187161hval_serializer.is_valid():
            v187161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v187161hval=V187161hvals.objects.get(id_presion_val=id)
        v187161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)       

class V272981hsApi(View):
      
    def post(self,request):
         
         v272981h_data=JSONParser().parse(request)
         v272981h_serializer=V272981hSerializer(data=v272981h_data)
         if v272981h_serializer.is_valid():
             v272981h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v272981hs = V272981hs.objects.all()
         v272981h_serializer=V272981hSerializer(v272981hs,many=True)
         return JsonResponse(v272981h_serializer.data,safe=False)

    def put(self,request):
         v272981h_data=JSONParser().parse(request)
         v272981h=V272981hs.objects.get(id_viento_rec=v272981h_data['id_viento_rec'])
         v272981h_serializer=V1073161hSerializer(v272981h,data=v272981h_data)
         if v272981h_serializer.is_valid():
            v272981h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v272981h=V272981hs.objects.get(id_viento_rec=id)
        v272981h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V272981hvalsApi(View):
      
    def post(self,request):
         
         v272981hval_data=JSONParser().parse(request)
         v272981hval_serializer=V272981hvalSerializer(data=v272981hval_data)
         if v272981hval_serializer.is_valid():
             v272981hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v272981hvals = V272981hvals.objects.all()
         v272981hval_serializer=V272981hvalSerializer(v272981hvals,many=True)
         return JsonResponse(v272981hval_serializer.data,safe=False)

    def put(self,request):
         v272981hval_data=JSONParser().parse(request)
         v272981hval=V272981hvals.objects.get(id_viento_rec_val=v272981hval_data['id_viento_rec_val'])
         v272981hval_serializer=V1073161hSerializer(v272981hval,data=v272981hval_data)
         if v272981hval_serializer.is_valid():
            v272981hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v272981hval=V272981hvals.objects.get(id_viento_rec_val=id)
        v272981hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V29311hsApi(View):
      
    def post(self,request):
         
         v29311h_data=JSONParser().parse(request)
         v29311h_serializer=V29311hSerializer(data=v29311h_data)
         if v29311h_serializer.is_valid():
             v29311h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v29311hs = V29311hs.objects.all()
         v29311h_serializer=V29311hSerializer(v29311hs,many=True)
         return JsonResponse(v29311h_serializer.data,safe=False)

    def put(self,request):
         v29311h_data=JSONParser().parse(request)
         v29311h=V29311hs.objects.get(id_temp_aire_max=v29311h_data['id_temp_aire_max'])
         v29311h_serializer=V1073161hSerializer(v29311h,data=v29311h_data)
         if v29311h_serializer.is_valid():
            v29311h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v29311h=V29311hs.objects.get(id_temp_aire_max=id)
        v29311h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V29311hvalsApi(View):
      
    def post(self,request):
         
         v29311hval_data=JSONParser().parse(request)
         v29311hval_serializer=V29311hvalSerializer(data=v29311hval_data)
         if v29311hval_serializer.is_valid():
             v29311hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v29311hvals = V29311hvals.objects.all()
         v29311hval_serializer=V29311hvalSerializer(v29311hvals,many=True)
         return JsonResponse(v29311hval_serializer.data,safe=False)

    def put(self,request):
         v29311hval_data=JSONParser().parse(request)
         v29311hval=V29311hvals.objects.get(id_temp_aire_max_val=v29311hval_data['id_temp_aire_max_val'])
         v29311hval_serializer=V1073161hSerializer(v29311hval,data=v29311hval_data)
         if v29311hval_serializer.is_valid():
            v29311hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v29311hval=V29311hvals.objects.get(id_temp_aire_max_val=id)
        v29311hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V29321hsApi(View):
      
    def post(self,request):
         
         v29321h_data=JSONParser().parse(request)
         v29321h_serializer=V29321hSerializer(data=v29321h_data)
         if v29321h_serializer.is_valid():
             v29321h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v29321hs = V29321hs.objects.all()
         v29321h_serializer=V29321hSerializer(v29321hs,many=True)
         return JsonResponse(v29321h_serializer.data,safe=False)

    def put(self,request):
         v29321h_data=JSONParser().parse(request)
         v29321h=V29321hs.objects.get(id_temp_aire_min=v29321h_data['id_temp_aire_min'])
         v29321h_serializer=V1073161hSerializer(v29321h,data=v29321h_data)
         if v29321h_serializer.is_valid():
            v29321h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v29321h=V29321hs.objects.get(id_temp_aire_min=id)
        v29321h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class V29321hvalsApi(View):
      
    def post(self,request):
         
         v29321hval_data=JSONParser().parse(request)
         v29321hval_serializer=V29321hvalSerializer(data=v29321hval_data)
         if v29321hval_serializer.is_valid():
             v29321hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v29321hvals = V29321hvals.objects.all()
         v29321hval_serializer=V29321hvalSerializer(v29321hvals,many=True)
         return JsonResponse(v29321hval_serializer.data,safe=False)

    def put(self,request):
         v29321hval_data=JSONParser().parse(request)
         v29321hval=V29321hvals.objects.get(id_temp_aire_min_val=v29321hval_data['id_temp_aire_min_val'])
         v29321hval_serializer=V1073161hSerializer(v29321hval,data=v29321hval_data)
         if v29321hval_serializer.is_valid():
            v29321hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v29321hval=V29321hvals.objects.get(id_temp_aire_min_val=id)
        v29321hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V303161hsApi(View):
      
    def post(self,request):
         
         v303161h_data=JSONParser().parse(request)
         v303161h_serializer=V303161hSerializer(data=v303161h_data)
         if v303161h_serializer.is_valid():
             v303161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v303161hs = V303161hs.objects.all()
         v303161h_serializer=V303161hSerializer(v303161hs,many=True)
         return JsonResponse(v303161h_serializer.data,safe=False)

    def put(self,request):
         v303161h_data=JSONParser().parse(request)
         v303161h=V303161hs.objects.get(id_temp_agua_mar=v303161h_data['id_temp_agua_mar'])
         v303161h_serializer=V1073161hSerializer(v303161h,data=v303161h_data)
         if v303161h_serializer.is_valid():
            v303161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v303161h=V303161hs.objects.get(id_temp_agua_mar=id)
        v303161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class V303161hvalsApi(View):
      
    def post(self,request):
         
         v303161hval_data=JSONParser().parse(request)
         v303161hval_serializer=V303161hvalSerializer(data=v303161hval_data)
         if v303161hval_serializer.is_valid():
             v303161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v303161hvals = V303161hvals.objects.all()
         v303161hval_serializer=V303161hvalSerializer(v303161hvals,many=True)
         return JsonResponse(v303161hval_serializer.data,safe=False)

    def put(self,request):
         v303161hval_data=JSONParser().parse(request)
         v303161hval=V303161hvals.objects.get(id_temp_agua_mar_val=v303161hval_data['id_temp_agua_mar_val'])
         v303161hval_serializer=V1073161hSerializer(v303161hval,data=v303161hval_data)
         if v303161hval_serializer.is_valid():
            v303161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v303161hval=V303161hvals.objects.get(id_temp_agua_mar_val=id)
        v303161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V42161hsApi(View):
      
    def post(self,request):
         
         v42161h_data=JSONParser().parse(request)
         v42161h_serializer=V42161hSerializer(data=v42161h_data)
         if v42161h_serializer.is_valid():
             v42161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v42161hs = V42161hs.objects.all()
         v42161h_serializer=V42161hSerializer(v42161hs,many=True)
         return JsonResponse(v42161h_serializer.data,safe=False)

    def put(self,request):
         v42161h_data=JSONParser().parse(request)
         v42161h=V42161hs.objects.get(id_viento_dir=v42161h_data['id_viento_dir'])
         v42161h_serializer=V1073161hSerializer(v42161h,data=v42161h_data)
         if v42161h_serializer.is_valid():
            v42161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v42161h=V42161hs.objects.get(id_viento_dir=id)
        v42161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class V42161hvalsApi(View):
      
    def post(self,request):
         
         v42161hval_data=JSONParser().parse(request)
         v42161hval_serializer=V42161hvalSerializer(data=v42161hval_data)
         if v42161hval_serializer.is_valid():
             v42161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v42161hvals = V42161hvals.objects.all()
         v42161hval_serializer=V42161hvalSerializer(v42161hvals,many=True)
         return JsonResponse(v42161hval_serializer.data,safe=False)

    def put(self,request):
         v42161hval_data=JSONParser().parse(request)
         v42161hval=V42161hvals.objects.get(id_viento_dir_val=v42161hval_data['id_viento_dir_val'])
         v42161hval_serializer=V1073161hSerializer(v42161hval,data=v42161hval_data)
         if v42161hval_serializer.is_valid():
            v42161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v42161hval=V42161hvals.objects.get(id_viento_dir_val=id)
        v42161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V557161hsApi(View):
      
    def post(self,request):
         
         v557161h_data=JSONParser().parse(request)
         v557161h_serializer=V557161hSerializer(data=v557161h_data)
         if v557161h_serializer.is_valid():
             v557161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v557161hs = V557161hs.objects.all()
         v557161h_serializer=V557161hSerializer(v557161hs,many=True)
         return JsonResponse(v557161h_serializer.data,safe=False)

    def put(self,request):
         v557161h_data=JSONParser().parse(request)
         v557161h=V557161hs.objects.get(id_pres_red=v557161h_data['id_pres_red'])
         v557161h_serializer=V1073161hSerializer(v557161h,data=v557161h_data)
         if v557161h_serializer.is_valid():
            v557161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v557161h=V557161hs.objects.get(id_pres_red=id)
        v557161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V557161hvalsApi(View):
      
    def post(self,request):
         
         v557161hval_data=JSONParser().parse(request)
         v557161hval_serializer=V557161hvalSerializer(data=v557161hval_data)
         if v557161hval_serializer.is_valid():
             v557161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v557161hvals = V557161hvals.objects.all()
         v557161hval_serializer=V557161hvalSerializer(v557161hvals,many=True)
         return JsonResponse(v557161hval_serializer.data,safe=False)

    def put(self,request):
         v557161hval_data=JSONParser().parse(request)
         v557161hval=V557161hvals.objects.get(id_pres_red_val=v557161hval_data['id_pres_red_val'])
         v557161hval_serializer=V1073161hSerializer(v557161hval,data=v557161hval_data)
         if v557161hval_serializer.is_valid():
            v557161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v557161hval=V557161hvals.objects.get(id_pres_red_val=id)
        v557161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V573161hsApi(View):
      
    def post(self,request):
         
         v573161h_data=JSONParser().parse(request)
         v573161h_serializer=V573161hSerializer(data=v573161h_data)
         if v573161h_serializer.is_valid():
             v573161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v573161hs = V573161hs.objects.all()
         v573161h_serializer=V573161hSerializer(v573161hs,many=True)
         return JsonResponse(v573161h_serializer.data,safe=False)

    def put(self,request):
         v573161h_data=JSONParser().parse(request)
         v573161h=V573161hs.objects.get(id_term_seco=v573161h_data['id_term_seco'])
         v573161h_serializer=V1073161hSerializer(v573161h,data=v573161h_data)
         if v573161h_serializer.is_valid():
            v573161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v573161h=V573161hs.objects.get(id_term_seco=id)
        v573161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V573161hvalsApi(View):
      
    def post(self,request):
         
         v573161hval_data=JSONParser().parse(request)
         v573161hval_serializer=V573161hvalSerializer(data=v573161hval_data)
         if v573161hval_serializer.is_valid():
             v573161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v573161hvals = V573161hvals.objects.all()
         v573161hval_serializer=V573161hvalSerializer(v573161hvals,many=True)
         return JsonResponse(v573161hval_serializer.data,safe=False)

    def put(self,request):
         v573161hval_data=JSONParser().parse(request)
         v573161hval=V573161hvals.objects.get(id_term_seco_val=v573161hval_data['id_term_seco_val'])
         v573161hval_serializer=V1073161hSerializer(v573161hval,data=v573161hval_data)
         if v573161hval_serializer.is_valid():
            v573161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v573161hval=V573161hvals.objects.get(id_term_seco_val=id)
        v573161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)   


class V583161hsApi(View):
      
    def post(self,request):
         
         v583161h_data=JSONParser().parse(request)
         v583161h_serializer=V583161hSerializer(data=v583161h_data)
         if v583161h_serializer.is_valid():
             v583161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v583161hs = V583161hs.objects.all()
         v583161h_serializer=V583161hSerializer(v583161hs,many=True)
         return JsonResponse(v583161h_serializer.data,safe=False)

    def put(self,request):
         v583161h_data=JSONParser().parse(request)
         v583161h=V583161hs.objects.get(id_term_hmd=v583161h_data['id_term_hmd'])
         v583161h_serializer=V1073161hSerializer(v583161h,data=v583161h_data)
         if v583161h_serializer.is_valid():
            v583161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v583161h=V583161hs.objects.get(id_term_hmd=id)
        v583161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V583161hvalsApi(View):
      
    def post(self,request):
         
         v583161hval_data=JSONParser().parse(request)
         v583161hval_serializer=V583161hvalSerializer(data=v583161hval_data)
         if v583161hval_serializer.is_valid():
             v583161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v583161hvals = V583161hvals.objects.all()
         v583161hval_serializer=V583161hvalSerializer(v583161hvals,many=True)
         return JsonResponse(v583161hval_serializer.data,safe=False)

    def put(self,request):
         v583161hval_data=JSONParser().parse(request)
         v583161hval=V583161hvals.objects.get(id_term_hmd_val=v583161hval_data['id_term_hmd_val'])
         v583161hval_serializer=V1073161hSerializer(v583161hval,data=v583161hval_data)
         if v583161hval_serializer.is_valid():
            v583161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v583161hval=V583161hvals.objects.get(id_term_hmd_val=id)
        v583161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V597161hsApi(View):
      
    def post(self,request):
         
         v597161h_data=JSONParser().parse(request)
         v597161h_serializer=V597161hSerializer(data=v597161h_data)
         if v597161h_serializer.is_valid():
             v597161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v597161hs = V597161hs.objects.all()
         v597161h_serializer=V597161hSerializer(v597161hs,many=True)
         return JsonResponse(v597161h_serializer.data,safe=False)

    def put(self,request):
         v597161h_data=JSONParser().parse(request)
         v597161h=V597161hs.objects.get(id_tension_vapor=v597161h_data['id_tension_vapor'])
         v597161h_serializer=V1073161hSerializer(v597161h,data=v597161h_data)
         if v597161h_serializer.is_valid():
            v597161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v597161h=V597161hs.objects.get(id_tension_vapor=id)
        v597161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)    


class V597161hvalsApi(View):
      
    def post(self,request):
         
         v597161hval_data=JSONParser().parse(request)
         v597161hval_serializer=V597161hvalSerializer(data=v597161hval_data)
         if v597161hval_serializer.is_valid():
             v597161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v597161hvals = V597161hvals.objects.all()
         v597161hval_serializer=V597161hvalSerializer(v597161hvals,many=True)
         return JsonResponse(v597161hval_serializer.data,safe=False)

    def put(self,request):
         v597161hval_data=JSONParser().parse(request)
         v597161hval=V597161hvals.objects.get(id_tension_vapor_val=v597161hval_data['id_tension_vapor_val'])
         v597161hval_serializer=V1073161hSerializer(v597161hval,data=v597161hval_data)
         if v597161hval_serializer.is_valid():
            v597161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v597161hval=V597161hvals.objects.get(id_tension_vapor_val=id)
        v597161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V603161hsApi(View):
      
    def post(self,request):
         
         v603161h_data=JSONParser().parse(request)
         v603161h_serializer=V603161hSerializer(data=v603161h_data)
         if v603161h_serializer.is_valid():
             v603161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v603161hs = V603161hs.objects.all()
         v603161h_serializer=V603161hSerializer(v603161hs,many=True)
         return JsonResponse(v603161h_serializer.data,safe=False)

    def put(self,request):
         v603161h_data=JSONParser().parse(request)
         v603161h=V603161hs.objects.get(id_punto_rocio=v603161h_data['id_punto_rocio'])
         v603161h_serializer=V1073161hSerializer(v603161h,data=v603161h_data)
         if v603161h_serializer.is_valid():
            v603161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v603161h=V603161hs.objects.get(id_punto_rocio=id)
        v603161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     

class V603161hvalsApi(View):
      
    def post(self,request):
         
         v603161hval_data=JSONParser().parse(request)
         v603161hval_serializer=V603161hvalSerializer(data=v603161hval_data)
         if v603161hval_serializer.is_valid():
             v603161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v603161hvals = V603161hvals.objects.all()
         v603161hval_serializer=V603161hvalSerializer(v603161hvals,many=True)
         return JsonResponse(v603161hval_serializer.data,safe=False)

    def put(self,request):
         v603161hval_data=JSONParser().parse(request)
         v603161hval=V603161hvals.objects.get(id_punto_rocio_val=v603161hval_data['id_punto_rocio_val'])
         v603161hval_serializer=V1073161hSerializer(v603161hval,data=v603161hval_data)
         if v603161hval_serializer.is_valid():
            v603161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v603161hval=V603161hvals.objects.get(id_punto_rocio_val=id)
        v603161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V614161hsApi(View):
      
    def post(self,request):
         
         v614161h_data=JSONParser().parse(request)
         v614161h_serializer=V614161hSerializer(data=v614161h_data)
         if v614161h_serializer.is_valid():
             v614161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v614161hs = V614161hs.objects.all()
         v614161h_serializer=V614161hSerializer(v614161hs,many=True)
         return JsonResponse(v614161h_serializer.data,safe=False)

    def put(self,request):
         v614161h_data=JSONParser().parse(request)
         v614161h=V614161hs.objects.get(id_evapo=v614161h_data['id_evapo'])
         v614161h_serializer=V1073161hSerializer(v614161h,data=v614161h_data)
         if v614161h_serializer.is_valid():
            v614161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v614161h=V614161hs.objects.get(id_evapo=id)
        v614161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V614161hvalsApi(View):
      
    def post(self,request):
         
         v614161hval_data=JSONParser().parse(request)
         v614161hval_serializer=V614161hvalSerializer(data=v614161hval_data)
         if v614161hval_serializer.is_valid():
             v614161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v614161hvals = V614161hvals.objects.all()
         v614161hval_serializer=V614161hvalSerializer(v614161hvals,many=True)
         return JsonResponse(v614161hval_serializer.data,safe=False)

    def put(self,request):
         v614161hval_data=JSONParser().parse(request)
         v614161hval=V614161hvals.objects.get(id_evapo_val=v614161hval_data['id_evapo_val'])
         v614161hval_serializer=V1073161hSerializer(v614161hval,data=v614161hval_data)
         if v614161hval_serializer.is_valid():
            v614161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v614161hval=V614161hvals.objects.get(id_evapo_val=id)
        v614161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False) 



class V644161hsApi(View):
      
    def post(self,request):
         
         v644161h_data=JSONParser().parse(request)
         v644161h_serializer=V644161hSerializer(data=v644161h_data)
         if v644161h_serializer.is_valid():
             v644161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v644161hs = V644161hs.objects.all()
         v644161h_serializer=V644161hSerializer(v644161hs,many=True)
         return JsonResponse(v644161h_serializer.data,safe=False)

    def put(self,request):
         v644161h_data=JSONParser().parse(request)
         v644161h=V644161hs.objects.get(id_nube=v644161h_data['id_nube'])
         v644161h_serializer=V1073161hSerializer(v644161h,data=v644161h_data)
         if v644161h_serializer.is_valid():
            v644161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v644161h=V644161hs.objects.get(id_nube=id)
        v644161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V644161hvalsApi(View):
      
    def post(self,request):
         
         v644161hval_data=JSONParser().parse(request)
         v644161hval_serializer=V644161hvalSerializer(data=v644161hval_data)
         if v644161hval_serializer.is_valid():
             v644161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v644161hvals = V644161hvals.objects.all()
         v644161hval_serializer=V644161hvalSerializer(v644161hvals,many=True)
         return JsonResponse(v644161hval_serializer.data,safe=False)

    def put(self,request):
         v644161hval_data=JSONParser().parse(request)
         v644161hval=V644161hvals.objects.get(id_nube_val=v644161hval_data['id_nube_val'])
         v644161hval_serializer=V1073161hSerializer(v644161hval,data=v644161hval_data)
         if v644161hval_serializer.is_valid():
            v644161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v644161hval=V644161hvals.objects.get(id_nube_val=id)
        v644161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V674161hsApi(View):
      
    def post(self,request):
         
         v674161h_data=JSONParser().parse(request)
         v674161h_serializer=V674161hSerializer(data=v674161h_data)
         if v674161h_serializer.is_valid():
             v674161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v674161hs = V674161hs.objects.all()
         v674161h_serializer=V674161hSerializer(v674161hs,many=True)
         return JsonResponse(v674161h_serializer.data,safe=False)

    def put(self,request):
         v674161h_data=JSONParser().parse(request)
         v674161h=V674161hs.objects.get(id_nube=v674161h_data['id_nube'])
         v674161h_serializer=V1073161hSerializer(v674161h,data=v674161h_data)
         if v674161h_serializer.is_valid():
            v674161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v674161h=V674161hs.objects.get(id_nube=id)
        v674161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V674161hvalsApi(View):
      
    def post(self,request):
         
         v674161hval_data=JSONParser().parse(request)
         v674161hval_serializer=V674161hvalSerializer(data=v674161hval_data)
         if v674161hval_serializer.is_valid():
             v674161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v674161hvals = V674161hvals.objects.all()
         v674161hval_serializer=V674161hvalSerializer(v674161hvals,many=True)
         return JsonResponse(v674161hval_serializer.data,safe=False)

    def put(self,request):
         v674161hval_data=JSONParser().parse(request)
         v674161hval=V674161hvals.objects.get(id_nube_val=v674161hval_data['id_nube_val'])
         v674161hval_serializer=V1073161hSerializer(v674161hval,data=v674161hval_data)
         if v674161hval_serializer.is_valid():
            v674161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v674161hval=V674161hvals.objects.get(id_nube_val=id)
        v674161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)    



class V704161hsApi(View):
      
    def post(self,request):
         
         v704161h_data=JSONParser().parse(request)
         v704161h_serializer=V704161hSerializer(data=v704161h_data)
         if v704161h_serializer.is_valid():
             v704161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v704161hs = V704161hs.objects.all()
         v704161h_serializer=V704161hSerializer(v704161hs,many=True)
         return JsonResponse(v704161h_serializer.data,safe=False)

    def put(self,request):
         v704161h_data=JSONParser().parse(request)
         v704161h=V704161hs.objects.get(id_nube=v704161h_data['id_nube'])
         v704161h_serializer=V1073161hSerializer(v704161h,data=v704161h_data)
         if v704161h_serializer.is_valid():
            v704161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v704161h=V704161hs.objects.get(id_nube=id)
        v704161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V704161hvalsApi(View):
      
    def post(self,request):
         
         v704161hval_data=JSONParser().parse(request)
         v704161hval_serializer=V704161hvalSerializer(data=v704161hval_data)
         if v704161hval_serializer.is_valid():
             v704161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v704161hvals = V704161hvals.objects.all()
         v704161hval_serializer=V704161hvalSerializer(v704161hvals,many=True)
         return JsonResponse(v704161hval_serializer.data,safe=False)

    def put(self,request):
         v704161hval_data=JSONParser().parse(request)
         v704161hval=V704161hvals.objects.get(id_nube_val=v704161hval_data['id_nube_val'])
         v704161hval_serializer=V1073161hSerializer(v704161hval,data=v704161hval_data)
         if v704161hval_serializer.is_valid():
            v704161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v704161hval=V704161hvals.objects.get(id_nube_val=id)
        v704161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)     


class V7229161hsApi(View):
      
    def post(self,request):
         
         v7229161h_data=JSONParser().parse(request)
         v7229161h_serializer=V7229161hSerializer(data=v7229161h_data)
         if v7229161h_serializer.is_valid():
             v7229161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v7229161hs = V7229161hs.objects.all()
         v7229161h_serializer=V7229161hSerializer(v7229161hs,many=True)
         return JsonResponse(v7229161h_serializer.data,safe=False)

    def put(self,request):
         v7229161h_data=JSONParser().parse(request)
         v7229161h=V7229161hs.objects.get(id_visibilidad_hor=v7229161h_data['id_visibilidad_hor'])
         v7229161h_serializer=V1073161hSerializer(v7229161h,data=v7229161h_data)
         if v7229161h_serializer.is_valid():
            v7229161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v7229161h=V7229161hs.objects.get(id_visibilidad_hor=id)
        v7229161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  



class V7229161hvalsApi(View):
      
    def post(self,request):
         
         v7229161hval_data=JSONParser().parse(request)
         v7229161hval_serializer=V7229161hvalSerializer(data=v7229161hval_data)
         if v7229161hval_serializer.is_valid():
             v7229161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v7229161hvals = V7229161hvals.objects.all()
         v7229161hval_serializer=V7229161hvalSerializer(v7229161hvals,many=True)
         return JsonResponse(v7229161hval_serializer.data,safe=False)

    def put(self,request):
         v7229161hval_data=JSONParser().parse(request)
         v7229161hval=V7229161hvals.objects.get(id_visibilidad_hor_val=v7229161hval_data['id_visibilidad_hor_val'])
         v7229161hval_serializer=V1073161hSerializer(v7229161hval,data=v7229161hval_data)
         if v7229161hval_serializer.is_valid():
            v7229161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v7229161hval=V7229161hvals.objects.get(id_visibilidad_hor_val=id)
        v7229161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class V7514161hsApi(View):
      
    def post(self,request):
         
         v7514161h_data=JSONParser().parse(request)
         v7514161h_serializer=V7514161hSerializer(data=v7514161h_data)
         if v7514161h_serializer.is_valid():
             v7514161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v7514161hs = V7514161hs.objects.all()
         v7514161h_serializer=V7514161hSerializer(v7514161hs,many=True)
         return JsonResponse(v7514161h_serializer.data,safe=False)

    def put(self,request):
         v7514161h_data=JSONParser().parse(request)
         v7514161h=V7514161hs.objects.get(id_reduc_tanque=v7514161h_data['id_reduc_tanque'])
         v7514161h_serializer=V1073161hSerializer(v7514161h,data=v7514161h_data)
         if v7514161h_serializer.is_valid():
            v7514161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v7514161h=V7514161hs.objects.get(id_reduc_tanque=id)
        v7514161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class V7514161hvalsApi(View):
      
    def post(self,request):
         
         v7514161hval_data=JSONParser().parse(request)
         v7514161hval_serializer=V7514161hvalSerializer(data=v7514161hval_data)
         if v7514161hval_serializer.is_valid():
             v7514161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v7514161hvals = V7514161hvals.objects.all()
         v7514161hval_serializer=V7514161hvalSerializer(v7514161hvals,many=True)
         return JsonResponse(v7514161hval_serializer.data,safe=False)

    def put(self,request):
         v7514161hval_data=JSONParser().parse(request)
         v7514161hval=V7514161hvals.objects.get(id_reduc_tanque_val=v7514161hval_data['id_reduc_tanque_val'])
         v7514161hval_serializer=V1073161hSerializer(v7514161hval,data=v7514161hval_data)
         if v7514161hval_serializer.is_valid():
            v7514161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v7514161hval=V7514161hvals.objects.get(id_reduc_tanque_val=id)
        v7514161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class V765161hsApi(View):
      
    def post(self,request):
         
         v765161h_data=JSONParser().parse(request)
         v765161h_serializer=V765161hSerializer(data=v765161h_data)
         if v765161h_serializer.is_valid():
             v765161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v765161hs = V765161hs.objects.all()
         v765161h_serializer=V765161hSerializer(v765161hs,many=True)
         return JsonResponse(v765161h_serializer.data,safe=False)

    def put(self,request):
         v765161h_data=JSONParser().parse(request)
         v765161h=V765161hs.objects.get(id_agua_sacada=v765161h_data['id_agua_sacada'])
         v765161h_serializer=V1073161hSerializer(v765161h,data=v765161h_data)
         if v765161h_serializer.is_valid():
            v765161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v765161h=V765161hs.objects.get(id_agua_sacada=id)
        v765161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class V765161hvalsApi(View):
      
    def post(self,request):
         
         v765161hval_data=JSONParser().parse(request)
         v765161hval_serializer=V765161hvalSerializer(data=v765161hval_data)
         if v765161hval_serializer.is_valid():
             v765161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v765161hvals = V765161hvals.objects.all()
         v765161hval_serializer=V765161hvalSerializer(v765161hvals,many=True)
         return JsonResponse(v765161hval_serializer.data,safe=False)

    def put(self,request):
         v765161hval_data=JSONParser().parse(request)
         v765161hval=V765161hvals.objects.get(id_agua_sacada_val=v765161hval_data['id_agua_sacada_val'])
         v765161hval_serializer=V1073161hSerializer(v765161hval,data=v765161hval_data)
         if v765161hval_serializer.is_valid():
            v765161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v765161hval=V765161hvals.objects.get(id_agua_sacada_val=id)
        v765161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class V775161hsApi(View):
      
    def post(self,request):
         
         v775161h_data=JSONParser().parse(request)
         v775161h_serializer=V775161hSerializer(data=v775161h_data)
         if v775161h_serializer.is_valid():
             v775161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v775161hs = V775161hs.objects.all()
         v775161h_serializer=V775161hSerializer(v775161hs,many=True)
         return JsonResponse(v775161h_serializer.data,safe=False)

    def put(self,request):
         v775161h_data=JSONParser().parse(request)
         v775161h=V775161hs.objects.get(id_agua_aniadida=v775161h_data['id_agua_aniadida'])
         v775161h_serializer=V1073161hSerializer(v775161h,data=v775161h_data)
         if v775161h_serializer.is_valid():
            v775161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v775161h=V775161hs.objects.get(id_agua_aniadida=id)
        v775161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  
        

class V775161hvalsApi(View):
      
    def post(self,request):
         
         v775161hval_data=JSONParser().parse(request)
         v775161hval_serializer=V775161hvalSerializer(data=v775161hval_data)
         if v775161hval_serializer.is_valid():
             v775161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v775161hvals = V775161hvals.objects.all()
         v775161hval_serializer=V775161hvalSerializer(v775161hvals,many=True)
         return JsonResponse(v775161hval_serializer.data,safe=False)

    def put(self,request):
         v775161hval_data=JSONParser().parse(request)
         v775161hval=V775161hvals.objects.get(id_agua_aniadida_val=v775161hval_data['id_agua_aniadida_val'])
         v775161hval_serializer=V1073161hSerializer(v775161hval,data=v775161hval_data)
         if v775161hval_serializer.is_valid():
            v775161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v775161hval=V775161hvals.objects.get(id_agua_aniadida_val=id)
        v775161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  


class V91161hsApi(View):
      
    def post(self,request):
         
         v91161h_data=JSONParser().parse(request)
         v91161h_serializer=V91161hSerializer(data=v91161h_data)
         if v91161h_serializer.is_valid():
             v91161h_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v91161hs = V91161hs.objects.all()
         v91161h_serializer=V91161hSerializer(v91161hs,many=True)
         return JsonResponse(v91161h_serializer.data,safe=False)

    def put(self,request):
         v91161h_data=JSONParser().parse(request)
         v91161h=V91161hs.objects.get(id_humedad_rltva=v91161h_data['id_humedad_rltva'])
         v91161h_serializer=V1073161hSerializer(v91161h,data=v91161h_data)
         if v91161h_serializer.is_valid():
            v91161h_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v91161h=V91161hs.objects.get(id_humedad_rltva=id)
        v91161h.delete()
        return JsonResponse("Deleted Successfully",safe=False)  



class V91161hvalsApi(View):
      
    def post(self,request):
         
         v91161hval_data=JSONParser().parse(request)
         v91161hval_serializer=V91161hvalSerializer(data=v91161hval_data)
         if v91161hval_serializer.is_valid():
             v91161hval_serializer.save()
             return JsonResponse('Se agrrego correctamente',safe=False)
         return   JsonResponse('No se pudo agregar ',safe=False) 
   
    def get(self,request):
         v91161hvals = V91161hvals.objects.all()
         v91161hval_serializer=V91161hvalSerializer(v91161hvals,many=True)
         return JsonResponse(v91161hval_serializer.data,safe=False)

    def put(self,request):
         v91161hval_data=JSONParser().parse(request)
         v91161hval=V91161hvals.objects.get(id_humedad_rltva_val=v91161hval_data['id_humedad_rltva_val'])
         v91161hval_serializer=V1073161hSerializer(v91161hval,data=v91161hval_data)
         if v91161hval_serializer.is_valid():
            v91161hval_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update")

    def delete(self,request,id):
        v91161hval=V91161hvals.objects.get(id_humedad_rltva_val=id)
        v91161hval.delete()
        return JsonResponse("Deleted Successfully",safe=False)  

   


 


     



  