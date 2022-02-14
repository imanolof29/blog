#DJANGO REST FRAMEWORK
from tkinter.ttk import Style
from django.forms import ValidationError
from rest_framework import serializers
#DJANGO
from django.contrib.auth import get_user_model, authenticate


class UserModelSerializer(serializers.ModelSerializer):
    """Serializer for the user model"""
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True, 'min_length':5}}
    
    def create(self, validated_data):
        return get_user_model().objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user



class AuthTokenSerializer(serializers.Serializer):
    """Serializer for user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('context'),
            username=email,
            password=password
        )

        if not user:
            raise ValidationError('Unable to authenticate with provided credentials')
        
        attrs['user'] = user
        return attrs