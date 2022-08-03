from rest_framework import serializers
from core.models import Headernames

class HeadernamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headernames
        fields = ['name', ]
