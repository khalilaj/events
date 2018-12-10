from rest_framework import serializers
from .models import SessionSpeaker

from ..user.serializer import AccountDetailSerializer
from ..user.models import Account

class RetrieveUpdateSerial(serializers.ModelSerializer):
    session_speaker_id = AccountDetailSerializer()

    class Meta:
        model = SessionSpeaker
        fields = '__all__'


class ListCreateSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SessionSpeaker
        fields = '__all__'

    def create(self, validated_data):
        return SessionSpeaker.objects.create(**validated_data)
