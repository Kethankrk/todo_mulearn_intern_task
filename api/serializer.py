from mvt.models import User, Todo
from rest_framework import serializers


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "created_at", "expire", "is_expired", "completed", "user"]
        read_only_fields = ['user']