from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
                                    #author = JournalistSerializer(read_only=True)
                                    #author = serializers.StringRelatedField()
    """Serialization Part"""
    class Meta:
        model = Article
        fields = "__all__"
                                   #fields = ("author","title","body",etc.) #include only
                                   #exclude = "id"                         # exclude

    """Validation Part"""
    def validate(self, data):
        """ Check author and title are not the same """
        if data["title"] == data["author"]:
            raise serializers.ValidationError("Author & Title should not the same!!")
        return data

    def validate_body(self, value):
        """ Check body should contain more than 5 chars"""
        if len(value) < 5:
            raise serializers.ValidationError("Should be more than 5 chars!!")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"


##Option to ModelSerializer
'''
class ArticleSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.active = validated_data.get('active', instance.active)
        instance.save()

        return instance

    def validate(self, data):
        """ Check author and title are not the same """
        if data["title"] == data["author"]:
            raise serializers.ValidationError("Author & Title should not the same!!")
        return data

    def validate_body(self, value):
        """ Check body should contain more than 5 chars"""
        if len(value) < 5:
            raise serializers.ValidationError("Should be more than 5 chars!!")
        return value
'''
