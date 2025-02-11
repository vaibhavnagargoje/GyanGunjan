from django.urls import path
from .views import (
    
    ThematicListCreateView, ThematicDetailView,
    MovieListCreateView, MovieDetailView,
    CoffeeTableBookListCreateView, CoffeeTableBookDetailView,
    StateListCreateView, StateDetailView,
    RegionListCreateView, RegionDetailView,
    FlipbookListCreateView, FlipbookDetailView,
    AboutProjectListCreateView, AboutProjectDetailView,LandingPageSectionList,LandingPageSectionDetail,
    JeevanDarshanSectionView
)


urlpatterns = [
    # Landing Page Data API
    path('api/landing-sections/', LandingPageSectionList.as_view(), name='landing-sections-list'),
    path('api/landing-sections/<str:section_type>/', LandingPageSectionDetail.as_view(), name='landing-section-detail'),


    # Jeevan Darshan API
    path('api/jeevan-darshan/', JeevanDarshanSectionView.as_view(), name='jeevan-darshan'),


    # Thematic API
    path('api/thematic/', ThematicListCreateView.as_view(), name='thematic-list-create'),
    path('api/thematic/<int:pk>/', ThematicDetailView.as_view(), name='thematic-detail'),

    # Coffee Table Book API
    path('api/coffee-table-books/', CoffeeTableBookListCreateView.as_view(), name='coffee-table-book-list-create'),
    path('api/coffee-table-books/<int:pk>/', CoffeeTableBookDetailView.as_view(), name='coffee-table-book-detail'),

    # Movie API
    path('api/movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    # State API
    path('api/states/', StateListCreateView.as_view(), name='state-list-create'),
    path('api/states/<int:pk>/', StateDetailView.as_view(), name='state-detail'),

    # Region API
    path('api/regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('api/regions/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),

    # Flipbook API
    path('api/flipbooks/', FlipbookListCreateView.as_view(), name='flipbook-list-create'),
    path('api/flipbooks/<int:pk>/', FlipbookDetailView.as_view(), name='flipbook-detail'),

    # About Project API
    path('api/about-project/', AboutProjectListCreateView.as_view(), name='about-project-list-create'),
    path('api/about-project/<int:pk>/', AboutProjectDetailView.as_view(), name='about-project-detail'),





]
