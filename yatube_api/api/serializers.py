from rest_framework import serializers

from posts.models import Group, Comment, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_field = ('post', 'author')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
