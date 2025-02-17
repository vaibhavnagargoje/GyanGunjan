from django.urls import path
from .views import ContributeListCreateView, ContributeDetailView

urlpatterns = [
    # API endpoints
    path('api/contributions/', ContributeListCreateView.as_view(), name='contribute-list-create'),
    path('api/contributions/<int:pk>/', ContributeDetailView.as_view(), name='contribute-detail'),
]