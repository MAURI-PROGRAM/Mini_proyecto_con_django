from django.contrib import admin
from .forms import RegModelForm
from .models import Resistrado


class AdminRegistrado(admin.ModelAdmin):
	list_display = ['id','__str__','nombre','timestamp']
	form=RegModelForm
	list_display_links=['id']
	list_filter=['timestamp']
	list_editable=['nombre']
	search_fields=['nombre']
admin.site.register(Resistrado,AdminRegistrado)