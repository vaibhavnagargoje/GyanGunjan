from django.contrib import admin
from .models import Thematic
from .models import Movie,CoffeeTableBook
from .models import State,Region,Flipbook
from.models import AboutProject,AboutProjectImage




admin.site.site_header = "Gyan Gunjan Admin"  # Change the header text
admin.site.site_title = "Gyan Gunjan Portal"  # Change the title on the browser tab
admin.site.index_title = "Welcome to Gyan Gunjan Dashboard"  # Change the index title
# Register your models here.


from .models import LandingPageSection, LandingImage

class LandingImageInline(admin.TabularInline):
    model = LandingImage
    extra = 1  # Number of empty image slots shown

@admin.register(LandingPageSection)
class LandingPageSectionAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'title')
    inlines = [LandingImageInline]
    fieldsets = (
        ('Section Identity', {
            'fields': ('section_type',)
        }),
        ('Content', {
            'fields': ('title', 'short_description', 'long_description', 'additional_text')
        }),
    )

@admin.register(LandingImage)
class LandingImageAdmin(admin.ModelAdmin):
    list_display = ('section', 'image_preview', 'caption')
    list_filter = ('section__section_type',)
    
    def image_preview(self, obj):
        return obj.image.url if obj.image else ''
    image_preview.short_description = 'Preview'





from django.contrib import admin
from .models import JeevanDarshanSection, JeevanDarshanImage

@admin.register(JeevanDarshanSection)
class JeevanDarshanSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'left_description', 'right_description')
    search_fields = ('title',)

@admin.register(JeevanDarshanImage)
class JeevanDarshanImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'short_description')
    search_fields = ('title', 'section__title')








@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_youtube_movie')
    search_fields = ('name',)

admin.site.register(Thematic)
admin.site.register(CoffeeTableBook)



admin.site.register(State)
admin.site.register(Region)
admin.site.register(Flipbook)


admin.site.register(AboutProject)
admin.site.register(AboutProjectImage)




