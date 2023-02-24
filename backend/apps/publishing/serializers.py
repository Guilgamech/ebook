from rest_framework import serializers

from apps.publishing.models import Publishing


class PublishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishing
        fields = '__all__'