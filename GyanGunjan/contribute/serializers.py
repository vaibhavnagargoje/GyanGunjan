from rest_framework import serializers
from .models import Contribute

class ContributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = '__all__'  # Include all fields from the model