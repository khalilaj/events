from rest_framework import serializers
from conference.conference.models import Conference


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'
        read_only_fields = ("id",)


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Conference
        fields = '__all__'
        read_only_fields = ("id",)

    def create(self, validated_data):
        return Conference.objects.create(**validated_data)
