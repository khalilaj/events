from rest_framework import serializers

from app.event.models import Event


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        return Event.objects.create(**validated_data)