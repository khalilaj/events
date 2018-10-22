from rest_framework import serializers
from .models import EventFeedback


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = EventFeedback
        fields = '__all__'
        read_only_fields = ("event_id",)


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EventFeedback
        fields = '__all__'
        read_only_fields = ("event_id",)

    def create(self, validated_data):
        return EventFeedback.objects.create(**validated_data)
