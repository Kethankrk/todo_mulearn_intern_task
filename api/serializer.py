from mvt.models import User
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