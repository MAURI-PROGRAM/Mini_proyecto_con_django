from django import forms
from .models import Resistrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model=Resistrado
		fields=['nombre','email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base,email_provide=email.split('@')
		dominio,extension=email_provide.split('.')
		if not "edu" in extension:
			raise forms.ValidationError("poner un .edu")
		return email

	def clean_nombre(self):
		nombre=self.cleaned_data.get("nombre")
		return nombre


class ContactForm(forms.Form):
	nombre=forms.CharField(required=False)
	email=forms.EmailField()
	mensaje=forms.CharField(widget=forms.Textarea)
	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base,email_provide=email.split('@')
		dominio,extension=email_provide.split('.')
		if not "edu" in extension:
			raise forms.ValidationError("poner un .edu")
		return email