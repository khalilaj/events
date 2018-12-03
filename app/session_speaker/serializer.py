from rest_framework import serializers
from .models import SessionSpeaker


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = SessionSpeaker
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionSpeaker
        fields = '__all__'

    def create(self, validated_data):
        return SessionSpeaker.objects.create(**validated_data)
