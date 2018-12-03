from rest_framework import serializers

from .models import SessionFeedback


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = SessionFeedback
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionFeedback
        fields = '__all__'

    def create(self, validated_data):
        return SessionFeedback.objects.create(**validated_data)
