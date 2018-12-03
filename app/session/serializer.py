from rest_framework import serializers

from .models import Session


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Session
        fields = '__all__'

    def create(self, validated_data):
        return Session.objects.create(**validated_data)
