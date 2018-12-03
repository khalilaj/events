from rest_framework import serializers

from app.conference_details.models import Conference


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Conference
        fields = '__all__'

    def create(self, validated_data):
        return Conference.objects.create(**validated_data)
