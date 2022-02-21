from django.db.models import fields
from django.db.models import ModelSerializer

from rest_framework import serializers
from backend.models import v1073161H
from backend.models import v1073161HVal
from backend.models import v1073161H 
from backend.models import v1073161HVal 
from backend.models import V1087161H 
from backend.models import V1087161HVal 
from backend.models import V1097161H 
from backend.models import V1097161HVal 
from backend.models import V1263011H 
from backend.models import V1263011HVal 
from backend.models import V12630161H 
from backend.models import V12630161HVal 
from backend.models import V1263021H  
from backend.models import V1263021HVal
from backend.models import V1263041H
from backend.models import V1263041HVal
from backend.models import V141011H
from backend.models import V141011HVal
from backend.models import V1410161H 
from backend.models import V1410161HVal 
from backend.models import V141021H  
from backend.models import V141021HVal 
from backend.models import V141041H  
from backend.models import V141041HVal  
from backend.models import V1714161H  
from backend.models import V1714161HVal 
from backend.models import V171481H 
from backend.models import V171481HVal 
from backend.models import V187161H 
from backend.models import V187161HVal 
from backend.models import V272981H 
from backend.models import V272981HVal 
from backend.models import V29311H 
from backend.models import V29311HVal 
from backend.models import V29321H 
from backend.models import V29321HVal 
from backend.models import V303161H 
from backend.models import V303161HVal 
from backend.models import V42161H 
from backend.models import V42161HVal 
from backend.models import V557161H 
from backend.models import V557161HVal 
from backend.models import V573161H 
from backend.models import V573161HVal 
from backend.models import V583161H 
from backend.models import V583161HVal 
from backend.models import V597161H 
from backend.models import V597161HVal 
from backend.models import V603161H  
from backend.models import V603161HVal 
from backend.models import V614161H 
from backend.models import V614161HVal 
from backend.models import V644161H 
from backend.models import V644161HVal 
from backend.models import V674161H 
from backend.models import V674161HVal 
from backend.models import V704161H 
from backend.models import V704161HVal 
from backend.models import V7229161H 
from backend.models import V7229161HVal
from backend.models import V7514161H
from backend.models import V7514161HVal
from backend.models import V765161H
from backend.models import V765161HVal
from backend.models import V775161H
from backend.models import V775161HVal  
from backend.models import V91161H 
from backend.models import V91161HVal 
from backend.models import Accesos
from backend.models import Cantones
from backend.models import Captores
from backend.models import CaptoresTipos
from backend.models import Categorias 
from backend.models import Cuencas
from backend.models import DireccionesViento
from backend.models import Distritos
from backend.models import DjangoMigrations 
from backend.models import Estaciones
from backend.models import EstadosEstacion
from backend.models import EstadosValidacion
from backend.models import FenomenosNaturales
from backend.models import GeneroNubes
from backend.models import MetodosAcceso
from backend.models import Parroquias
from backend.models import ProfundidadesGeotemp
from backend.models import Propietarios 
from backend.models import Provincias
from backend.models import PuntosObservacion
from backend.models import Regiones
from backend.models import TipoEstaciones
from backend.models import TipoGeotemperaturas
from backend.models import TiposCalculoEvap
from backend.models import UnidadesMedida
from backend.models import Usuarios
from backend.models import Zonas  

class v1073161HSerializer(serializers.ModelSerializer): 
    class Meta: 
         model=v1073161H
         fields = '__all__'

class v1073161HValSerializer(serializers.ModelSerializer): 
    class Meta: 
         model=v1073161HVal
         fields = '__all__'

class V1087161HSerializer(serializers.ModelSerializer): 
     class Meta: 
          model=V1087161H
          fields = '__all__'
 
class V1087161HValSerializer(serializers.ModelSerializer): 
     class Meta: 
          model=V1087161HVal
          fields = '__all__'
class V1097161HSerializer(serializers.ModelSerializer): 
     class Meta: 
          model=V1097161H
          fields = '__all__'

class V1097161HValSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1097161HVal
          fields = '__all__'

class V1263011HSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1263011H
          fields = '__all__'
 
class V1263011HValSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1263011HVal
          fields = '__all__'
 
class V12630161HSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V12630161H
          fields = '__all__'
 
class V12630161HValSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V12630161HVal
          fields = '__all__'
class V1263021HSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1263021H
          fields = '__all__'

class V1263021HValSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1263021HVal
          fields = '__all__'

class V1263041HSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1263041H
          fields = '__all__'

class V1263041HValSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V1263041HVal
          fields = '__all__'

class V141011HSerializer(serializers.ModelSerializer): 
   class Meta: 
          model=V141011H
          fields = '__all__'

class V141011HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V141011HVal
          fields = '__all__'
class V1410161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V1410161H
          fields = '__all__'
class V1410161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V1410161HVal
          fields = '__all__'
class V141021HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V141021H
          fields = '__all__'
class V141021HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V141021HVal
          fields = '__all__'
class V141041HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V141041H
          fields = '__all__'

class V141041HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V141041HVal
          fields = '__all__'

class V1714161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V1714161H
          fields = '__all__'

class V1714161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V1714161HVal
          fields = '__all__'

class V171481HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V171481H
          fields = '__all__'

class V171481HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V171481HVal
          fields = '__all__'
 
class V187161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V187161H
          fields = '__all__'
class V187161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V187161HVal
          fields = '__all__'

class V272981HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V272981H
          fields = '__all__'

class V272981HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V272981HVal
          fields = '__all__'
class V29311HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V29311H
          fields = '__all__'
class V29311HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V29311HVal
          fields = '__all__'

class V29321HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V29321H
          fields = '__all__'
class V29321HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V29321HVal
          fields = '__all__'
class V303161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V303161H
          fields = '__all__'
class V303161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V303161HVal
          fields = '__all__'

class V42161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V42161H
          fields = '__all__'

class V42161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V42161HVal
          fields = '__all__'
class V557161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V557161H
          fields = '__all__'
class V557161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V557161HVal
          fields = '__all__'
class V573161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V573161H
          fields = '__all__'

class V573161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V573161HVal
          fields = '__all__'

class V583161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V583161H
          fields = '__all__'
class V583161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V583161HVal
          fields = '__all__'
class V597161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V597161H
          fields = '__all__'
class V597161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V597161HVal
          fields = '__all__'
class V603161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V603161H
          fields = '__all__'
class V603161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V603161HVal
          fields = '__all__'
class V614161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V614161H
          fields = '__all__'

class V614161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V614161HVal
          fields = '__all__'
class V644161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V644161H
          fields = '__all__'
class V644161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V644161HVal
          fields = '__all__'
class V674161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V674161H
          fields = '__all__'
class V674161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V674161HVal
          fields = '__all__'
class V704161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V704161H
          fields = '__all__'
class V704161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V704161HVal
          fields = '__all__'
class V7229161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V7229161H
          fields = '__all__'

class V7229161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V7229161HVal
          fields = '__all__'
class V7514161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V7514161H
          fields = '__all__'
class V7514161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V7514161HVal
          fields = '__all__'
class V765161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V765161H
          fields = '__all__'
class V765161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V765161HVal
          fields = '__all__'
class V775161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V775161H
          fields = '__all__'
class V775161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V775161HVal
          fields = '__all__'
class V91161HSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V91161H
          fields = '__all__'
class V91161HValSerializer(serializers.ModelSerializer):  
   class Meta: 
          model=V91161HVal
          fields = '__all__'

       

 
 
 

 