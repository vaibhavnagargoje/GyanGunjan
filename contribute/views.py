from rest_framework import generics
from .models import Contribute
from .serializers import ContributeSerializer

# API view to list all contributions or create a new one
class ContributeListCreateView(generics.ListCreateAPIView):
    queryset = Contribute.objects.all()
    serializer_class = ContributeSerializer

# API view to retrieve, update, or delete a specific contribution
class ContributeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribute.objects.all()
    serializer_class = ContributeSerializer