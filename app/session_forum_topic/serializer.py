from rest_framework import serializers

from .models import SessionForumTopic


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = SessionForumTopic
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionForumTopic
        fields = '__all__'

    def create(self, validated_data):
        return SessionForumTopic.objects.create(**validated_data)
