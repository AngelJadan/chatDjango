from django.db import models

class  Salas(models.Model):
    sal_id = models.AutoField(primary_key=True)
    sal_codigo = models.CharField(max_length=250, unique=True)
    salas_sal_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.sal_codigo
    
class Usuarios(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nombre = models.CharField(max_length=250)
    usu_apellido = models.CharField(max_length=250)
    usu_usuario = models.CharField(max_length=250, unique=True)
    usu_pass = models.CharField(max_length=250)
    usu_correo = models.EmailField()
    def __str__(self):
        return self.usu_usuario
    
class Mensajes(models.Model):
    men_id = models.AutoField(primary_key=True)
    men_mensaje = models.CharField(max_length=250, blank=False, null=False)
    salas_sal_id = models.ForeignKey(Salas,on_delete=models.CASCADE, null=False, blank=False)
    men_remit = models.ForeignKey(Usuarios,on_delete=models.CASCADE, null=False, blank=False)
    def __int__ (self):
        return self.men_id

class  Usu_Salas(models.Model):
    usa_id = models.AutoField(primary_key=True)
    usuarios_usu_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE,null=False, blank=False)
    salas_sal_id = models.ForeignKey(Salas, on_delete=models.CASCADE, null=False, blank=False)
    def __int__(self):
        return self.usa_id