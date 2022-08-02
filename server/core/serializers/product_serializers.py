from dataclasses import field
from rest_framework import serializers
from core.models import *


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'url', 'logowidth', 'logoheight']


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributenames
        fields = ['name', ]


class HeadernamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headernames
        fields = ['name', ]


class ProductAttributeSerializer(serializers.ModelSerializer):
    attributeid = AttributeNameSerializer(read_only=True)

    class Meta:
        model = Productattribute
        fields = ['attributeid',
                  'displayvalue', 'type', 'isabsolute', 'setnumber']


class ProductDescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdescriptions
        fields = ['type',  'description', ]


class ProductFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productfeatures
        fields = ['text', 'ordernumber', ]


class ProductLocalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productlocales
        fields = ['status', ]


class ProductSkusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productskus
        fields = ['name', 'sku']


class ProductElementPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productelementproperties
        fields = ['propertykey', 'propertyvalue']


class ProductElementsSerializer(serializers.ModelSerializer):
    productElementProperties = ProductElementPropertiesSerializer(many=True)

    class Meta:
        model = Productelements
        fields = ['type', 'status', 'productElementProperties']


class ProductAccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productaccessories
        fields = ['productid', ]


class HeaderNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headernames
        exclude = ['localeid', 'headerid']


class CategoryHeaderSerializer(serializers.ModelSerializer):
    headerid = HeaderNamesSerializer()

    class Meta:
        model = Categoryheader
        fields = ['headerid', 'displayorder']


class CategoryDisplayAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorydisplayattributes
        exclude = ['cat_id', 'isactive']


class CategorySerializer(serializers.ModelSerializer):
    categoryDisplayAttributeValue = CategoryDisplayAttributesSerializer(
        many=True)
    categoryHeader = CategoryHeaderSerializer(many=True)

    class Meta:
        model = Category
        fields = ['categoryHeader', 'categoryDisplayAttributeValue']


class ProductSerializer(serializers.ModelSerializer):
    manufacturerid = ManufacturerSerializer(read_only=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True)
    productElements = ProductElementsSerializer(many=True)
    productAttribute = ProductAttributeSerializer(many=True)
    productFeatures = ProductFeaturesSerializer(many=True)
    productSkus = ProductSkusSerializer(many=True)
    productLocale = ProductLocalesSerializer(many=True)
    categoryid = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'categoryid',
            'manufacturerid',
            'mfgpartno',
            'isaccessory',
            'productDescription',
            'productElements',
            'productAttribute',
            'productFeatures',
            'productSkus',
            'productLocale',
        ]


class SearchAttributeValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchAttributeValues
        fields = ['value', ]
