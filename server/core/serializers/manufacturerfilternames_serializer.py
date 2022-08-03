from rest_framework import serializers
from core.models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'url', 'logowidth', 'logoheight']
