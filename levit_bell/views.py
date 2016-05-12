# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect

def inicio(request):
	return render(request, 'index.html') #Agarra la ruta templates/index.html

def politicas_privacidad(request):
	return render(request, 'politicas_priv.html') #Agarra la ruta templates/index.html

def politica_empresarial(request):
	return render(request, 'politica_empresarial.html')