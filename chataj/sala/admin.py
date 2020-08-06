from django.contrib import admin
from .models import Usuarios, Salas, Usu_Salas, Mensajes
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Salas)
admin.site.register(Usu_Salas)
admin.site.register(Mensajes)