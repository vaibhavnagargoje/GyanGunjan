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





from rest_framework import serializers
from .models import JeevanDarshanSection, JeevanDarshanImage, CoffeeTableBook, Thematic

class JeevanDarshanImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = JeevanDarshanImage
        fields = ['image_url', 'title', 'short_description']

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if obj.image else None

class CoffeeTableBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeTableBook
        fields = ['id','coffee_table_book_name', 'description', 'book_pdf', 'cover_image']

   

   

class ThematicSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Thematic
        fields = ['id','name', 'headline', 'cover_picture','book_pdf']

class JeevanDarshanSectionSerializer(serializers.ModelSerializer):
    images = JeevanDarshanImageSerializer(many=True, read_only=True)
    coffee_table_book = CoffeeTableBookSerializer(source='related_coffee_table_book', read_only=True)
    thematic = ThematicSerializer(source='related_thematic', read_only=True)

    class Meta:
        model = JeevanDarshanSection
        fields = [
            'title', 'short_description', 'left_description', 'right_description',
            'images', 'coffee_table_book', 'thematic'
        ]




class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'youtube_link', 'uploaded_movie','movie_thumbnail']


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
        fields = ['id', 'title', 'description', 'state', 'region', 'book_pdf','cover_image']






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
        fields = ['id', 'title', 'tag', 'description_left', 'description_right', 'logo_image', 'images','long_discripton','first_discripton','first_discripton_image','fifth_discripton_image','second_description','second_discripton_image','third_description','third_discripton_image','fourth_description','fourth_discripton_image','fifth_description','sixth_description','sixth_discripton_image']