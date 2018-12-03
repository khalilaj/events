from rest_framework import serializers

from .models import SessionForumResponses


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = SessionForumResponses
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionForumResponses
        fields = '__all__'

    def create(self, validated_data):
        return SessionForumResponses.objects.create(**validated_data)
