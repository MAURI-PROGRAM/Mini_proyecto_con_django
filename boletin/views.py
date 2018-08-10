from django.shortcuts import render
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
		print(form.cleaned_data)
	context={
		'el_form': form,
	}
	return render(request,'form1.html',context)