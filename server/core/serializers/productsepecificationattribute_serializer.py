from rest_framework import serializers
from core.models import Productattribute
from core.models import Productattribute, Categorydisplayattributes


class ProductSpecificationAttributeSerializer(serializers.ModelSerializer):
    """ Productattribute Model serializer including child other model. 
    like attributenames."""

    atrribute_label = serializers.CharField(
        read_only=True, source='attributeid.name')
    header_id = serializers.SerializerMethodField()

    def get_header_id(self, obj):
        obj = Categorydisplayattributes.objects.filter(
            categoryid=obj.productid.categoryid,
            attributeid=obj.attributeid).values_list('headerid', flat=True).distinct()

        return obj[0]

    class Meta:
        model = Productattribute
        fields = [
            'type',
            'header_id',
            'attributeid',
            'displayvalue',
            'atrribute_label'
        ]
