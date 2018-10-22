from rest_framework import serializers
from .models import EventAttendant


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = EventAttendant
        fields = '__all__'
        read_only_fields = ("event_id",)


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EventAttendant
        fields = '__all__'
        read_only_fields = ("event_id",)

    def create(self, validated_data):
        return EventAttendant.objects.create(**validated_data)
