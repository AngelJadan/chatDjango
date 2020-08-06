from rest_framework import serializers
from .models import Salas, Usuarios, Mensajes, Usu_Salas

class SalasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salas
        fields = ('sal_id','sal_codigo','salas_sal_id')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('usu_id','usu_nombre','usu_apellido', 'usu_usuario',
        'usu_pass','usu_correo')

class  MensajesSerializer(serializers.ModelSerializer):
    model = Mensajes
    fields = ('men_d','men_mensaje','salas_sal_id','men_remit')

class UsuSalSerializer(serializers.ModelsSerializer):
    model = Usu_Salas
    fields = ('usa_id','usuarios_usu_id','salas_sal_id')