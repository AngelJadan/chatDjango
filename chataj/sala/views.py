from django.shortcuts import render, redirect
from .models import Usuarios, Mensajes, Salas
from .forms import UsuariosForms, MesajesForms, SalasForms, UsuSalaForms, Usu_Salas


def indice(request):
    return render(request, 'sala/indice.html')
def sala(request, room_name):
    return render(request, 'sala/sala.html', {
        'room_name': room_name
    })
def login(request):
    return render(request,'sala/login.html')
def iniUser(request):
    if request.GET["user"] and request.GET["pass"]:
        usu = request.GET["user"]
        pas = request.GET["pass"]
        
        usuario = Usuarios.objects.filter(usu_usuario__contains=usu)
        pasw = Usuarios.objects.filter(usu_pass=pas)
        contex = {'usuarios':usuario}
        ren=render(request,"sala/inicioUsuario.html",contex)
        #try:
        #except :
            #ren=render(request,"sala/login.html")
        #ren=render(request,"inicioUsuario.html")
    else:
        ren=render(request,"sala/inicioUsuario.html",contex)
        #ren=HttpResponse(mensaje)
    return ren
def contactos(request):
    if request.method=='POST':
        form = UsuariosForms(request.POST)
def regUsuario(request):
    if request.method == 'GET':
        form = UsuariosForms()
        conexto = {
            'form':form
        }
    else:
        form = UsuariosForms(request.POST)
        conexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect("login")
        print(form)
    return render(request,'sala/registrarUsuario.html', conexto)
def envSms(request):
    form = MensajesForms(request.POST)
    contex = {
        'form':form
    }
    return render(request,'sala/inicioUsuario.html',contex)
def crearSala(request):
    form = SalasForms()
    cont = {
        'form':form
    }
    if form.is_valid():
        form.save()
        return redirect('sala/inicioUsuario.html')
def unirUserSala(request):
    form = UsuSalaForms()
    cont = {
        'form':form
    }
def listarSalas(request):
    from django.db import connection
    from collections import namedtuple
    
    with connection.cursor() as cursor:
        cursor.execute('''SELECT s.sal_id ,s.sal_codigo codigo
         FROM sala_usuarios u, sala_usu_salas a, sala_salas s
        WHERE u.usu_usuario='Angel' AND u.usu_id = a.usuarios_usu_id_id AND s.sal_id = a.salas_sal_id_id
        ''')
        rowData = cursor.fetchall()
        result=[]
        for r in rowData:
            result.append(list(r))
            print(result)
        contexto = {'consultas': result}
    return render(request,'sala/salas.html',contexto)