from rest_framework import serializers
from .models import Tag


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
