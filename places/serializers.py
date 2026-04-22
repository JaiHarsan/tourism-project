from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.Serializer):
    """Serializer for Place model (MongoEngine)"""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    location = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    image = serializers.CharField(required=False, allow_null=True)
    rating = serializers.FloatField(default=4.5)
    
    def create(self, validated_data):
        """Create a new Place in MongoDB"""
        place = Place(**validated_data)
        place.save()
        return place
    
    def update(self, instance, validated_data):
        """Update an existing Place in MongoDB"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance