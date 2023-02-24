from rest_framework import serializers

from apps.gender.models import Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class GenderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'
