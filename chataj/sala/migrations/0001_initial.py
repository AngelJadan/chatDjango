# Generated by Django 3.0 on 2020-08-06 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('sal_id', models.AutoField(primary_key=True, serialize=False)),
                ('sal_codigo', models.CharField(max_length=250, unique=True)),
                ('salas_sal_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sala.Salas')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usu_id', models.AutoField(primary_key=True, serialize=False)),
                ('usu_nombre', models.CharField(max_length=250)),
                ('usu_apellido', models.CharField(max_length=250)),
                ('usu_usuario', models.CharField(max_length=250, unique=True)),
                ('usu_pass', models.CharField(max_length=250)),
                ('usu_correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Usu_Salas',
            fields=[
                ('usa_id', models.AutoField(primary_key=True, serialize=False)),
                ('salas_sal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala.Salas')),
                ('usuarios_usu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala.Usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('men_id', models.AutoField(primary_key=True, serialize=False)),
                ('men_mensaje', models.CharField(max_length=250)),
                ('men_remit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala.Usuarios')),
                ('salas_sal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala.Salas')),
            ],
        ),
    ]
