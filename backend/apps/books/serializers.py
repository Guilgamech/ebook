from rest_framework import serializers

from apps.author.serializers import AuthorSerializer
from apps.books.models import Books, Comment, Rating
from apps.gender.serializers import GenderReadSerializer
from apps.publishing.serializers import PublishingSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'date_create', 'book']
        read_only_fields = ['id', 'date_create', 'book']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BookReadSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publishing = PublishingSerializer()
    comment = CommentSerializer()
    rating = RatingSerializer()
    gender = GenderReadSerializer(many=True)

    class Meta:
        model = Books
        fields = '__all__'


