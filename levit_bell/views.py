# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect

def inicio(request):
	return render(request, 'index.html') #Agarra la ruta templates/index.html