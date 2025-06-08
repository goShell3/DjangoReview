from rest_framework import serializers
from rest_framework.serializers import SerializerMetaclass
from .models import Person

# class PersonSerializers(serializers.Serializer):
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Person(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get("fist_name", instance.first_name)
#         instance.last_name = validated_data.get("last_name", instance.last_name)
#         instance.save()
#         return instance

class PersonSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fieds = ['first_name', 'last_name']