from rest_framework import serializers

from .models import ConferenceAttendants


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = ConferenceAttendants
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConferenceAttendants
        fields = '__all__'

    def create(self, validated_data):
        return ConferenceAttendants.objects.create(**validated_data)
