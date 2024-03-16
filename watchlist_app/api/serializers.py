#we will map each field in serializers instead of using the model class
from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(self, value):
    if len(value) < 2:
        raise serializers.ValidationError("name is too short")
    else:
        return value

class MovieSerializer(serializers.Serializer):
    #validator
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    #field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value
        
    #object validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("title & description should not be the same")
        return data
    