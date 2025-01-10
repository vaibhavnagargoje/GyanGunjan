from django.shortcuts import render
from .models import Thematic

def home(request):
    # Define tabs and their corresponding keys
    tabs = ['thematic', 'coffee', 'regional', 'movies']

    # Determine the active tab from the request, default to 'thematic'
    active_tab = request.GET.get('active_tab', 'thematic')

    # Data for each tab
    thematic_resources = Thematic.objects.all() if active_tab == 'thematic' else []
    regional_resources = []  # Replace with query logic when the model is available
    movie_resources = []     # Replace with query logic when the model is available

    # Context to render in the template
    context = {
        'tabs': tabs,
        'active_tab': active_tab,
        'thematic_resources': thematic_resources,
        'regional_resources': regional_resources,
        'movie_resources': movie_resources,
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
