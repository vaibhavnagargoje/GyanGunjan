from django.contrib import admin
from .models import Thematic
from .models import LandingImages,LandingPageData,Movie,CoffeeTableBook
from .models import State,Region,Flipbook
from.models import AboutProject

# Register your models here.



# @admin.register(Contribute)
# class ContributeAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email',)
#     search_fields = ('first_name', 'last_name', 'email')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_youtube_movie')
    search_fields = ('name',)

admin.site.register(Thematic)
admin.site.register(LandingImages)
admin.site.register(LandingPageData)
admin.site.register(CoffeeTableBook)



admin.site.register(State)
admin.site.register(Region)
admin.site.register(Flipbook)


admin.site.register(AboutProject)




