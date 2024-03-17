#we will map each field in serializers instead of using the model class
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review
from rest_framework import viewsets

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ("watchlist",)
    
class WatchListSerializer(serializers.ModelSerializer):
    #crete, update, delete is automatically defined using ModelSerializer!
    # len_name = serializers.SerializerMethodField()
    # len_description = serializers.SerializerMethodField()
    
    #review_watchlist ==> when using get method only
    reviews_watchlist = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

# class StreamPlatformSerializer(serializers.ModelSerializer):
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # options = serializers.HyperlinkedRelatedField(view_name='stream-page', ready_only=True)
    # lookup_field = 'slug',
    # many=True,
    # read_only=True)
    #show complete details

    platform_watchlist = WatchListSerializer(many=True, read_only=True)
    
    #show only details in __str__
    # platform_watchlist = serializers.StringRelatedField(many=True, read_only=True)
    
    #show primary key
    # platform_watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    #hyperlinked
    # platform_watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-detail-page')
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    

    # def get_len_name(self, object):
    #     return len(object.name)
    
    # def get_len_description(self, object):
    #     return len(object.description)

    # # field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("name is too short")

# class MovieSerializer(serializers.Serializer):
#     #validator
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    #field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value
        
    #object validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("title & description should not be the same")
    #     return data
    