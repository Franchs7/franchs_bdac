from rest_framework import serializers
class LoginSerializer(serializers.ModelSerializer):
    name = serializers.SlugField()