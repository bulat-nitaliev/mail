from rest_framework import serializers
from general.models import User, Message, Secret, Attach
from rest_framework.serializers import BaseSerializer




class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name"
        )
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]          
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name"
        )

class SecretSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Secret
        fields = ('login',
                'password')
        # exclude = []
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('name',
                'dt_depart',
                'dt_receipt',
                'description')
        # exclude = []
        depth = 1

class AttachSerializer(serializers.ModelSerializer):
    # last_message = serializers.SerializerMethodField()
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Attach
        fields = ["pk", "file", "message"]
        depth = 1
