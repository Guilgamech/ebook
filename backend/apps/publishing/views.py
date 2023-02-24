from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.publishing.models import Publishing
from apps.publishing.serializers import PublishingSerializer


class PublishingViewSet(viewsets.ModelViewSet):
    queryset = Publishing.objects.all()
    serializer_class = PublishingSerializer
    permission_classes = (IsAuthenticated,)