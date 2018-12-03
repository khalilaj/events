from rest_framework import serializers

from .models import SessionMaterial


class RetrieveUpdateSerial(serializers.ModelSerializer):
    class Meta:
        model = SessionMaterial
        fields = '__all__'
        read_only_fields = ("session_id",)


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionMaterial
        fields = '__all__'
        read_only_fields = ("session_id", )

    def create(self, validated_data):
        return SessionMaterial.objects.create(**validated_data)
