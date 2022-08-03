from rest_framework import serializers
from core.models import Categoryheader
from core.serializers import HeaderNamesSerializer


class CategoryHeaderSerializer(serializers.ModelSerializer):
    headerid = HeaderNamesSerializer()

    class Meta:
        model = Categoryheader
        fields = ['headerid', 'displayorder']
