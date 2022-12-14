from rest_framework import serializers
from core.models import Productattribute
from core.models import Productattribute, Categorydisplayattributes


class ProductAttributeSerializer(serializers.ModelSerializer):
    """ Productattribute Model serializer including child other model. 
    like attributenames."""

    atrribute_label = serializers.CharField(
        read_only=True, source='attributeid.name')

    class Meta:
        model = Productattribute
        fields = [
            'type',
            # 'header_id',
            'attributeid',
            'displayvalue',
            'atrribute_label'
        ]
