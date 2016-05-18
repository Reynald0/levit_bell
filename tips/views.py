from django.shortcuts import render
from django.utils import timezone
from .models import Tip

def mas_tips(request):
	#Todos los tips ordenados por fecha de publicacion mas reciente
	tips = Tip.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
	return render(request, 'mas_tips.html', {'tips' : tips})
