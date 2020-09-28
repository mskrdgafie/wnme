from . import models
from rest_framework  import serializers
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User( first_name=validated_data['first_name'],last_name=validated_data['last_name'],email=validated_data['email'], username=validated_data['username'] )
		user.set_password(validated_data['password'])
		user.save()
		Token.objects.create(user=user)
		return user
