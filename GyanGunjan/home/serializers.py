from rest_framework import serializers
from .models import (
     Thematic, Movie, 
    CoffeeTableBook, State, Region, Flipbook, AboutProject
)


# serilizers 
from .models import LandingPageSection, LandingImage

class LandingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingImage
        fields = ['image', 'caption']

class LandingPageSectionSerializer(serializers.ModelSerializer):
    images = LandingImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = LandingPageSection
        fields = [
            'section_type', 
            'title', 
            'short_description', 
            'long_description', 
            'additional_text', 
            'images'
        ]




#for jeevan darshan
from rest_framework import serializers
from .models import JeevanDarshanSection, JeevanDarshanImage

# serializers.py
class JeevanDarshanImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = JeevanDarshanImage
        fields = ['image_url', 'title', 'short_description']  # Updated field names

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)

class JeevanDarshanSectionSerializer(serializers.ModelSerializer):
    images = JeevanDarshanImageSerializer(many=True, read_only=True)

    class Meta:
        model = JeevanDarshanSection
        fields = ['title', 'short_description', 'left_description', 'right_description', 'images']  # Added all fields











class ThematicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thematic
        fields = ['id', 'name', 'headline', 'cover_picture']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'youtube_link', 'uploaded_movie','movie_thumbnail']

class CoffeeTableBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeTableBook
        fields = ['id', 'coffee_table_book_name', 'description', 'book_pdf', 'cover_image']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name']

class RegionSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Region
        fields = ['id', 'name', 'state']

class FlipbookSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Flipbook
        fields = ['id', 'title', 'description', 'state', 'region', 'file','cover_image']






# serilizers for about project
from rest_framework import serializers
from .models import AboutProject, AboutProjectImage

class AboutProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProjectImage
        fields = ['id', 'image', 'alt_text']

class AboutProjectSerializer(serializers.ModelSerializer):
    images = AboutProjectImageSerializer(many=True, read_only=True)  # Nested serializer for images

    class Meta:
        model = AboutProject
        fields = ['id', 'title', 'tag', 'description_left', 'description_right', 'logo_image', 'images']