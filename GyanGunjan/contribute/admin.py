from django.contrib import admin
from . models import Contribute
# Register your models here.


@admin.register(Contribute)
class ContributeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email')
