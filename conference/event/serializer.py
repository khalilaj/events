from rest_framework import serializers
from .models import Event


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ("id", "conference_id")


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ("id", "conference_id")

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
