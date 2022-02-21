# Generated by Django 3.2.9 on 2022-01-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='V1073161hs',
            fields=[
                ('id_temp_int_baro', models.AutoField(primary_key=True, serialize=False)),
                ('id_estacion', models.IntegerField()),
                ('id_unidad_medida', models.IntegerField()),
                ('id_usuario', models.IntegerField()),
                ('fecha_toma', models.DateTimeField()),
                ('fecha_ingreso', models.DateTimeField()),
                ('valor', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
            ],
            options={
                'db_table': '_1073161h',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='v1073161H',
        ),
    ]
