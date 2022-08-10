from core.models import Categoryheader
from rest_framework import serializers


class CategoryHeaderSerializer(serializers.ModelSerializer):
    """ Categoryheader Model serializer including header_label from headername model."""

    header_label = serializers.CharField(
        read_only=True, source='headerid.name')

    class Meta:
        model = Categoryheader
        fields = [
            'headerid',
            'displayorder',
            'header_label'
        ]
