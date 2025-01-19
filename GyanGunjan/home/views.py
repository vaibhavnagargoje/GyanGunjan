from django.shortcuts import render
from .models import Thematic

from django.shortcuts import render
from .models import LandingPageData, LandingImages




def home(request):
    # Define tabs and their corresponding keys
    tabs = ['thematic', 'coffee', 'regional', 'movies']

    # Determine the active tab from the request, default to 'thematic'
    active_tab = request.GET.get('active_tab', 'thematic')

    # Fetch the landing page data and images
    landing_page_data = LandingPageData.objects.first()  # Assuming you're fetching the first entry
    landing_images = LandingImages.objects.filter(landing_page=landing_page_data)

    # Data for each tab
    thematic_resources = Thematic.objects.all() if active_tab == 'thematic' else []
    regional_resources = []  # Replace with query logic when the model is available
    movie_resources = []     # Replace with query logic when the model is available

    print(landing_page_data)
    # Context to render in the template
    context = {
        'tabs': tabs,
        'active_tab': active_tab,
        'thematic_resources': thematic_resources,
        'regional_resources': regional_resources,
        'movie_resources': movie_resources,
        'landing_images': landing_images,
        'landing_page_data':landing_page_data
    }

    return render(request, 'home/home.html', context)


from django.shortcuts import render
from .models import State, Region, Flipbook

def filter_flipbooks(request):
    states = State.objects.all()
    selected_state = request.GET.get("state")
    selected_region = request.GET.get("region")

    regions = Region.objects.filter(state__id=selected_state) if selected_state else Region.objects.none()
    flipbooks = Flipbook.objects.filter(state__id=selected_state)
    
    if selected_region:
        flipbooks = flipbooks.filter(region__id=selected_region)

    return render(request, "home/filter_flipbook.html", {
        "states": states,
        "regions": regions,
        "flipbooks": flipbooks,
    })






from .models import AboutProject
from django.shortcuts import render, get_object_or_404

def about_project(request):
    about_project = AboutProject.objects.first()
    landing_page_data = LandingPageData.objects.first()  # Assuming you're fetching the first entry
    landing_images = LandingImages.objects.filter(landing_page=landing_page_data)
    print(landing_images)
    context = {
        'about_project': about_project,
        'landing_images': landing_images,
    }
    return render(request, 'home/about_project.html', context)

 