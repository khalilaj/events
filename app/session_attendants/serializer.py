from rest_framework import serializers

from .models import SessionAttendants


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = SessionAttendants
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionAttendants
        fields = '__all__'

    def create(self, validated_data):
        return SessionAttendants.objects.create(**validated_data)
