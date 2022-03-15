from abc import abstractclassmethod
from datetime import date
from django.db import models



class Tabstrac(models.Model):
    id_temp_int_baro = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
   
    class Meta:
        abstract =True 
        
       

class T1073161hs(Tabstrac):

    class Meta:
        managed = False
        db_table = '_1073161h'


class T1073161hvals(models.Model):
    id_temp_int_baro_val = models.AutoField(primary_key=True)
    id_temp_int_baro = models.ForeignKey(T1073161hs, models.DO_NOTHING, db_column='id_temp_int_baro', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1073161h_val'


class T1087161hs(models.Model):
    id_pres_corre = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1087161h'


class T1087161hvals(models.Model):
    id_pres_corre_val = models.AutoField(primary_key=True)
    id_pres_corre = models.ForeignKey(T1087161hs, models.DO_NOTHING, db_column='id_pres_corre', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1087161h_val'


class T1097161hs(models.Model):
    id_pres_conv = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1097161h'


class T1097161hvals(models.Model):
    id_pres_conv_val = models.AutoField(primary_key=True)
    id_pres_conv = models.ForeignKey(T1097161hs, models.DO_NOTHING, db_column='id_pres_conv', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1097161h_val'


class T1263011hs(models.Model):
    id_caudal_max_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1263011h'


class T1263011hvals(models.Model):
    id_caudal_max_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T1263011hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1263011h_val'


class T12630161hs(models.Model):
    id_caudal_ins_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_12630161h'


class T12630161hvals(models.Model):
    id_caudal_ins_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T12630161hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_12630161h_val'


class T1263021hs(models.Model):
    id_caudal_min_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1263021h'


class T1263021hvals(models.Model):
    id_caudal_min_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T1263021hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1263021h_val'


class T1263041hs(models.Model):
    id_caudal_prom_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1263041h'


class T1263041hvals(models.Model):
    id_caudal_prom_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T1263041hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1263041h_val'


class T141011hs(models.Model):
    id_nivelagua_max_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_141011h'


class T141011hvals(models.Model):
    id_nivelagua_max_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T141011hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_141011h_val'


class T1410161hs(models.Model):
    id_nivelagua_ins_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1410161h'


class T1410161hvals(models.Model):
    id_nivelagua_ins_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T1410161hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1410161h_val'


class T141021hs(models.Model):
    id_nivelagua_min_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_141021h'


class T141021hvals(models.Model):
    id_nivelagua_min_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T141021hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_141021h_val'


class T141041hs(models.Model):
    id_nivelagua_prom_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_141041h'


class T141041hvals(models.Model):
    id_nivelagua_prom_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T141041hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_141041h_val'


class T1714161hs(models.Model):
    id_prec_1h = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1714161h'


class T1714161hvals(models.Model):
    id_prec_1h_val = models.AutoField(primary_key=True)
    id_prec_1h = models.ForeignKey(T1714161hs, models.DO_NOTHING, db_column='id_prec_1h', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_1714161h_val'


class T171481hs(models.Model):
    id_prec = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_171481h'


class T171481hvals(models.Model):
    id_prec_val = models.AutoField(primary_key=True)
    id_prec = models.ForeignKey(T171481hs, models.DO_NOTHING, db_column='id_prec', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_171481h_val'


class T187161hs(models.Model):
    id_presion = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_187161h'


class T187161hvals(models.Model):
    id_presion_val = models.AutoField(primary_key=True)
    id_presion = models.ForeignKey(T187161hs, models.DO_NOTHING, db_column='id_presion', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_187161h_val'


class T272981hs(models.Model):
    id_viento_rec = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_272981h'


class T272981hvals(models.Model):
    id_viento_rec_val = models.AutoField(primary_key=True)
    id_viento_rec = models.ForeignKey(T272981hs, models.DO_NOTHING, db_column='id_viento_rec', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_272981h_val'


class T29311hs(models.Model):
    id_temp_aire_max = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_29311h'


class T29311hvals(models.Model):
    id_temp_aire_max_val = models.AutoField(primary_key=True)
    id_temp_aire_max = models.ForeignKey(T29311hs, models.DO_NOTHING, db_column='id_temp_aire_max', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_29311h_val'


class T29321hs(models.Model):
    id_temp_aire_min = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_29321h'


class T29321hvals(models.Model):
    id_temp_aire_min_val = models.AutoField(primary_key=True)
    id_temp_aire_min = models.ForeignKey(T29321hs, models.DO_NOTHING, db_column='id_temp_aire_min', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_29321h_val'


class T303161hs(models.Model):
    id_temp_agua_mar = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_303161h'


class T303161hvals(models.Model):
    id_temp_agua_mar_val = models.AutoField(primary_key=True)
    id_temp_agua_mar = models.ForeignKey(T303161hs, models.DO_NOTHING, db_column='id_temp_agua_mar', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_303161h_val'


class T42161hs(models.Model):
    id_viento_dir = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    id_dir_viento = models.IntegerField()
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_42161h'


class T42161hvals(models.Model):
    id_viento_dir_val = models.AutoField(primary_key=True)
    id_viento_dir = models.ForeignKey(T42161hs, models.DO_NOTHING, db_column='id_viento_dir')
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    id_dir_viento = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_42161h_val'


class T557161hs(models.Model):
    id_pres_red = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_557161h'


class T557161hvals(models.Model):
    id_pres_red_val = models.AutoField(primary_key=True)
    id_pres_red = models.ForeignKey(T557161hs, models.DO_NOTHING, db_column='id_pres_red', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_557161h_val'


class T573161hs(models.Model):
    id_term_seco = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_573161h'


class T573161hvals(models.Model):
    id_term_seco_val = models.AutoField(primary_key=True)
    id_term_seco = models.ForeignKey(T573161hs, models.DO_NOTHING, db_column='id_term_seco', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_573161h_val'


class T583161hs(models.Model):
    id_term_hmd = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_583161h'


class T583161hvals(models.Model):
    id_term_hmd_val = models.AutoField(primary_key=True)
    id_term_hmd = models.ForeignKey(T583161hs, models.DO_NOTHING, db_column='id_term_hmd', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_583161h_val'


class T597161hs(models.Model):
    id_tension_vapor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_597161h'


class T597161hvals(models.Model):
    id_tension_vapor_val = models.AutoField(primary_key=True)
    id_tension_vapor = models.ForeignKey(T597161hs, models.DO_NOTHING, db_column='id_tension_vapor')
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_597161h_val'


class T603161hs(models.Model):
    id_punto_rocio = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_603161h'


class T603161hvals(models.Model):
    id_punto_rocio_val = models.CharField(primary_key=True, max_length=10)
    id_punto_rocio = models.ForeignKey(T603161hs, models.DO_NOTHING, db_column='id_punto_rocio', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_603161h_val'


class T614161hs(models.Model):
    id_evapo = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_614161h'

   


class T614161hvals(models.Model):
    id_evapo_val = models.AutoField(primary_key=True)
    id_evapo = models.ForeignKey(T614161hs, models.DO_NOTHING, db_column='id_evapo', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_614161h_val'


class T644161hs(models.Model):
    id_nube = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    altura_suelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_644161h'


class T644161hvals(models.Model):
    id_nube_val = models.AutoField(primary_key=True)
    id_nube = models.ForeignKey(T644161hs, models.DO_NOTHING, db_column='id_nube', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    altura_suelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_644161h_val'


class T674161hs(models.Model):
    id_nube = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    altura_suelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_674161h'


class T674161hvals(models.Model):
    id_nube_val = models.AutoField(primary_key=True)
    id_nube = models.ForeignKey(T674161hs, models.DO_NOTHING, db_column='id_nube', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    altura_suelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_674161h_val'


class T704161hs(models.Model):
    id_nube = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    altura_suelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_704161h'


class T704161hvals(models.Model):
    id_nube_val = models.AutoField(primary_key=True)
    id_nube = models.ForeignKey(T704161hs, models.DO_NOTHING, db_column='id_nube', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)
    altura_suelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_704161h_val'


class T7229161hs(models.Model):
    id_visibilidad_hor = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7229161h'


class T7229161hvals(models.Model):
    id_visibilidad_hor_val = models.AutoField(primary_key=True)
    id_visibilidad_hor = models.ForeignKey(T7229161hs, models.DO_NOTHING, db_column='id_visibilidad_hor', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7229161h_val'


class T7514161hs(models.Model):
    id_reduc_tanque = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7514161h'


class T7514161hvals(models.Model):
    id_reduc_tanque_val = models.AutoField(primary_key=True)
    id_reduc_tanque = models.ForeignKey(T7514161hs, models.DO_NOTHING, db_column='id_reduc_tanque', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_7514161h_val'


class T765161hs(models.Model):
    id_agua_sacada = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_765161h'


class T765161hvals(models.Model):
    id_agua_sacada_val = models.AutoField(primary_key=True)
    id_agua_sacada = models.ForeignKey(T765161hs, models.DO_NOTHING, db_column='id_agua_sacada', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_765161h_val'


class T775161hs(models.Model):
    id_agua_aniadida = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_775161h'


class T775161hvals(models.Model):
    id_agua_aniadida_val = models.AutoField(primary_key=True)
    id_agua_aniadida = models.ForeignKey(T775161hs, models.DO_NOTHING, db_column='id_agua_aniadida', blank=True, null=True)
    id_usuario = models.IntegerField()
    id_estado = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_775161h_val'


class T91161hs(models.Model):
    id_humedad_rltva = models.AutoField(primary_key=True)
    id_estacion = models.IntegerField()
    id_unidad_medida = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_toma = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_91161h'


class T91161hvals(models.Model):
    id_humedad_rltva_val = models.AutoField(primary_key=True)
    id_humedad_rltva = models.ForeignKey(T91161hs, models.DO_NOTHING, db_column='id_humedad_rltva', blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_91161h_val'

class Accesos(models.Model):
    id_acceso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accesos'


class Cantones(models.Model):
    id_canton = models.CharField(primary_key=True, max_length=4)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia')
    id_distrito = models.ForeignKey('Distritos', models.DO_NOTHING, db_column='id_distrito', blank=True, null=True)
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantones'


class Captores(models.Model):
    id_captor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'captores'


class CaptoresTipos(models.Model):
    id_captor_tipo = models.IntegerField(primary_key=True)
    id_captor = models.ForeignKey(Captores, models.DO_NOTHING, db_column='id_captor')
    id_tipo_estacion = models.ForeignKey('TipoEstaciones', models.DO_NOTHING, db_column='id_tipo_estacion')

    class Meta:
        managed = False
        db_table = 'captores_tipos'
        unique_together = (('id_captor_tipo', 'id_captor', 'id_tipo_estacion'),)


class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Cuencas(models.Model):
    codigo = models.CharField(max_length=8, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    id_cuenca = models.CharField(primary_key=True, max_length=5)
    nivel = models.IntegerField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuencas'


class DireccionesTiento(models.Model):
    id_dir_viento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    abreviacion = models.CharField(max_length=5)
    grados = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'direcciones_viento'


class Distritos(models.Model):
    id_distrito = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=600)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distritos'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Estaciones(models.Model):
    id_estacion = models.IntegerField(primary_key=True)
    id_estado_estacion = models.ForeignKey('EstadosEstacion', models.DO_NOTHING, db_column='id_estado_estacion')
    id_propietario = models.ForeignKey('Propietarios', models.DO_NOTHING, db_column='id_propietario')
    id_punto_obs = models.ForeignKey('PuntosObservacion', models.DO_NOTHING, db_column='id_punto_obs')
    id_captor_tipo = models.ForeignKey(CaptoresTipos, models.DO_NOTHING, db_column='id_captor_tipo')
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_levantamiento = models.DateField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    informacion = models.TextField(blank=True, null=True)
    dataloger = models.TextField(blank=True, null=True)
    img_norte = models.BinaryField(blank=True, null=True)
    img_sur = models.BinaryField(blank=True, null=True)
    img_este = models.BinaryField(blank=True, null=True)
    img_oeste = models.BinaryField(blank=True, null=True)
    vista_interna = models.BooleanField(blank=True, null=True)
    vista_externa = models.BooleanField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso1 = models.DateTimeField(blank=True, null=True)
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estaciones'
        unique_together = (('id_punto_obs', 'id_captor_tipo'),)


class EstadosEstacion(models.Model):
    id_estado_estacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_estacion'


class EstadosTalidacion(models.Model):
    id_estado_validacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_validacion'


class FenomenosNaturales(models.Model):
    id_fen_nat = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=110, blank=True, null=True)
    icono = models.BinaryField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fenomenos_naturales'


class GeneroNubes(models.Model):
    id_genero_nube = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    icono = models.BinaryField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    cifrado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero_nubes'


class MetodosAcceso(models.Model):
    id_metodo_acceso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'metodos_acceso'


class Parroquias(models.Model):
    id_parroquia = models.CharField(primary_key=True, max_length=6)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton')
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquias'


class ProfundidadesGeotemp(models.Model):
    id_profundidad_geotemp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'profundidades_geotemp'


class Propietarios(models.Model):
    id_propietario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    representante = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    informe = models.CharField(max_length=100, blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietarios'


class Provincias(models.Model):
    id_provincia = models.CharField(primary_key=True, max_length=4)
    id_region = models.ForeignKey('Regiones', models.DO_NOTHING, db_column='id_region')
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona')
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias'


class PuntosObservacion(models.Model):
    id_punto_obs = models.IntegerField(primary_key=True)
    id_cuenca = models.ForeignKey(Cuencas, models.DO_NOTHING, db_column='id_cuenca')
    id_parroquia = models.ForeignKey(Parroquias, models.DO_NOTHING, db_column='id_parroquia')
    id_acceso = models.ForeignKey(Accesos, models.DO_NOTHING, db_column='id_acceso')
    id_metodo_acceso = models.ForeignKey(MetodosAcceso, models.DO_NOTHING, db_column='id_metodo_acceso')
    codigo = models.CharField(unique=True, max_length=8)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    img_norte = models.BinaryField(blank=True, null=True)
    img_sur = models.BinaryField(blank=True, null=True)
    img_este = models.BinaryField(blank=True, null=True)
    img_oeste = models.BinaryField(blank=True, null=True)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puntos_observacion'


class Regiones(models.Model):
    id_region = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regiones'


class TipoEstaciones(models.Model):
    id_tipo_estacion = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
    nombre = models.CharField(max_length=50)
    observacion = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    codigo = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_estaciones'


class TipoGeotemperaturas(models.Model):
    id_tipo_geotemp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tipo_geotemperaturas'


class TiposCalculoEvap(models.Model):
    id_tipo_calculo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipos_calculo_evap'


class UnidadesMedida(models.Model):
    id_unidad_medida = models.IntegerField(primary_key=True)
    simbolo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    us_ingreso = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    us_modificacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades_medida'


class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasenia = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    persona_fk = models.BigIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    conv = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuarios'


class Zonas(models.Model):
    id_zona = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    us_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField()
    us_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas'



