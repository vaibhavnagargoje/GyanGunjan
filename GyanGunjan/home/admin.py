from django.contrib import admin
from .models import Thematic
from .models import Movie,CoffeeTableBook
from .models import State,Region,Flipbook
from.models import AboutProject,AboutProjectImage

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




# jeevan darshan models
from django.contrib import admin
from .models import JeevanDarshanSection, JeevanDarshanImage

class JeevanDarshanImageInline(admin.TabularInline):
    model = JeevanDarshanImage
    extra = 5  # Shows exactly 5 image fields (for your 5 images)
    max_num = 5  # Maximum allowed images
    min_num = 5  # Minimum required images

@admin.register(JeevanDarshanSection)
class JeevanDarshanSectionAdmin(admin.ModelAdmin):
    inlines = [JeevanDarshanImageInline]
    list_display = ('section_title',)
    
@admin.register(JeevanDarshanImage)
class JeevanDarshanImageAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'section')
    list_filter = ('section',)









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




