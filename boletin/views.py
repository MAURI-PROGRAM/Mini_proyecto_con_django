from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Resistrado
from .forms import RegModelForm,ContactForm

# Create your views here.
def inicio(request):

	if request.user.is_authenticated():
		form=RegModelForm(request.POST or None)
		titulo='HOlA'
		titulo='Bienvenido %s'%(request.user)
		context={
			'temp_titulo':titulo,
			'el_form':form,
		}
		if form.is_valid():
			instance=form.save(commit=False)
			nombre=form.cleaned_data.get('nombre')
			if not instance.nombre:
				instance.nombre='PERSONA'
			instance.save()
			context={
				'temp_titulo':'gracias %s' %(nombre) ,
			}
			
			print(instance)
			print(instance.timestamp)
			# form_data=form.cleaned_data
			# abc=form_data.get('email')
			# abc2=form_data.get('nombre')
			# obj=Resistrado.objects.create(email=abc,nombre=abc2)

	
		return render(request,'inicio.html',context)
	else:
		return render(request,'inicio.html')

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		email_to=form.cleaned_data.get('email')
		mensaje=form.cleaned_data.get('mensaje')
		nombre=form.cleaned_data.get('nombre')
		asunto='form de contactos'
		email_from=settings.EMAIL_HOST_USER
		mensaje_email=mensaje

		send_mail(asunto,
			mensaje_email,
			email_from,
			[email_to],
			fail_silently=False
			)
		
		# for key in form.cleaned_data:
		# 	print(key)
		# 	print(form.cleaned_data.get(key))

		# for key,value  in form.cleaned_data.items():
		# 	print(key,value)
		
		# print(email,mensaje,nombre)
	context={
		'el_form': form,
	}
	return render(request,'form1.html',context)