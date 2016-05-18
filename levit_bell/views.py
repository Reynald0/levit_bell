# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.utils import timezone
from tips.models import Tip

def inicio(request):
	#Primeros cuatro registros ordenados por fecha reciente
	tips = Tip.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')[0:4]
	# Se envia la variable tips al index pero en realidad se usa en el html ---> tips.html 
	# ----------> REVISAR el HTML TIPS.HTML
	return render(request, 'index.html', {'tips' : tips}) #Agarra la ruta templates/index.html

def politicas_privacidad(request):
	return render(request, 'politicas_priv.html') #Agarra la ruta templates/index.html

def politica_empresarial(request):
	return render(request, 'politica_empresarial.html')