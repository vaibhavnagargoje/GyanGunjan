from rest_framework import generics
from .models import ( Thematic, Movie, 
    CoffeeTableBook, State, Region, Flipbook, AboutProject
)
from .serializers import (
     ThematicSerializer, MovieSerializer, 
    CoffeeTableBookSerializer, StateSerializer, RegionSerializer, 
    FlipbookSerializer, AboutProjectSerializer
)


from .models import LandingPageSection
from .serializers import LandingPageSectionSerializer

class LandingPageSectionList(generics.ListAPIView):
    queryset = LandingPageSection.objects.prefetch_related('images').all()
    serializer_class = LandingPageSectionSerializer

class LandingPageSectionDetail(generics.RetrieveAPIView):
    queryset = LandingPageSection.objects.prefetch_related('images').all()
    serializer_class = LandingPageSectionSerializer
    lookup_field = 'section_type'



#jevan darshan
from rest_framework import generics
from .models import JeevanDarshanSection
from .serializers import JeevanDarshanSectionSerializer

from rest_framework import generics
from .models import JeevanDarshanSection
from .serializers import JeevanDarshanSectionSerializer

from rest_framework import generics
from rest_framework.response import Response
from .models import JeevanDarshanSection
from .serializers import JeevanDarshanSectionSerializer
#login_reqired import 
from django.contrib.auth.decorators import login_required

class JeevanDarshanSectionView(generics.ListAPIView):
    """
    API view to return all Jeevan Darshan Sections with related Coffee Table Books and Thematic content.
    """
    serializer_class = JeevanDarshanSectionSerializer
    queryset = JeevanDarshanSection.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Override the list method to explicitly pass the request context
        to the serializer so that media URLs are properly generated.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)



# Thematic API
class ThematicListCreateView(generics.ListCreateAPIView):
    queryset = Thematic.objects.all()
    serializer_class = ThematicSerializer

class ThematicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thematic.objects.all()
    serializer_class = ThematicSerializer


# Coffee Table Book API
class CoffeeTableBookListCreateView(generics.ListCreateAPIView):
    queryset = CoffeeTableBook.objects.all()
    serializer_class = CoffeeTableBookSerializer

class CoffeeTableBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoffeeTableBook.objects.all()
    serializer_class = CoffeeTableBookSerializer




# Movie API
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# State API
class StateListCreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

# Region API
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# Flipbook API
class FlipbookListCreateView(generics.ListCreateAPIView):
    queryset = Flipbook.objects.all()
    serializer_class = FlipbookSerializer

class FlipbookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flipbook.objects.all()
    serializer_class = FlipbookSerializer

# About Project API
class AboutProjectListCreateView(generics.ListCreateAPIView):
    queryset = AboutProject.objects.all()
    serializer_class = AboutProjectSerializer

class AboutProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutProject.objects.all()
    serializer_class = AboutProjectSerializer