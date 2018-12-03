from rest_framework import serializers

from .models import ConferenceFeedback


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = ConferenceFeedback
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConferenceFeedback
        fields = '__all__'

    def create(self, validated_data):
        return ConferenceFeedback.objects.create(**validated_data)
