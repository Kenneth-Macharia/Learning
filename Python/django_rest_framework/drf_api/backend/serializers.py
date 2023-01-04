from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """ Automatically maps to model fields, and implements model validators and abstract
    methods e.g create and update
    """
    # Read-only fields are included in the API output, but should not be included in the
    # input during create or update operations.
    # Not added to POST payload as its is dynamically generated but if not added
    # as a read-only field the serializer validation will fail
    slug = serializers.SlugField(read_only=True)
    # auto adds user name to articles
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = '__all__'  # or a list of fields to serialize


# class ArticleSerializer(serializers.Serializer):
#     """ For serializers.Serializer, all fields must be explicitly specified """
#
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(read_only=True)
#     published = serializers.DateField(read_only=True)
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.published = validated_data.get('published', instance.published)
#         instance.save()
#         return instance

    # Implementing the the serializers via django shell
    # from io import BytesIO
    # from backend.models import Article
    # from rest_framework.renderers import JSONRenderer
    # from rest_framework.parsers import JSONParser
    # from backend.serializers import ArticleSerializer
    #
    # a = Article(title='serialized article', description='serialized article descritpion')
    # a.save()
    #
    # ---------------- Serialization --------------
    # serializer = ArticleSerializer(a)
    # json_content = JSONRenderer().render(serializer.data)
    #
    # ---------------- deserialization --------------
    # byte_stream = BytesIO(json_content)
    # data = JSONParser().parse(byte_stream)
    # serializer = ArticleSerializer(data=data)
    # serializer.is_valid()
    # serializer.validated_data

