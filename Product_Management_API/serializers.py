from django.contrib.auth.models import User
from rest_framework import serializers
from Product_Management_API.models import ProductDb

class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductDb
        fields = "__all__"
        read_only_fields = ["user"]