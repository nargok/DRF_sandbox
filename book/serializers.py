from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Book
    fields = ('title', 'price', 'created_at',)

  def create(self, validated_data):
    """
    Create a new Book
    """
    return Book.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
    Update an existing Snippet instance
    """

    instance.title = validated_data.get('title', instance.title)
    instance.price = validated_data.get('price', instance.code)
    instance.save()
    return instance
