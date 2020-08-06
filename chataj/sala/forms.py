from django import forms
from .models import Usuarios, Salas, Mensajes, Usu_Salas


class MesajesForms(forms.ModelForm):
    class Meta:
        model = Mensajes
        fields = [
            'men_mensaje','salas_sal_id','men_remit'
        ]
        labels = {
            'men_mensaje':'Mensaje',
            'salas_sal_id':'SubSala',
            'men_remit':'Remitente',
        }
class UsuariosForms(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            'usu_id','usu_nombre','usu_apellido','usu_usuario','usu_pass','usu_correo'
        ]
        labels = {
            'usu_id':'id',
            'usu_nombre':'Nombre',
            'usu_apellido':'Apellido',
            'usu_usuario':'Usuario',
            'usu_pass':'Password',
            'usu_correo':'Email',
        }
        widgets = {
            'usu_nombre':forms.TextInput(attrs={'class':'form-control'}),
            'usu_apellido':forms.TextInput(attrs={'class':'form-control'}),
            'usu_usuario':forms.TextInput(attrs={'class':'form-control'}),
            'usu_pass':forms.TextInput(attrs={'class':'form-control'}),
            'usu_correo':forms.TextInput(attrs={'class':'form-control'}),
        }
class SalasForms(forms.ModelForm):
    class Meta:
        model = Salas
        fields = [
            'sal_codigo','salas_sal_id'
        ]
        labels = {
            'sal_codigo':'codigo',
            'salas_sal_id':'sala',
        }
class  UsuSalaForms(forms.ModelForm):
    class  Meta:
        model = Usu_Salas
        fields =[
            'usa_id','usuarios_usu_id','salas_sal_id'
        ]
        labels = {
            'usa_id':'IdUsuario',
            'usuarios_usu_id':'usuario',
            'salas_sal_id':'sala',
        }