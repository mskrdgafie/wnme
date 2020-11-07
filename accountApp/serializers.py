from . import models
from rest_framework  import serializers
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#sendinblue
from .mailin import Mailin


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User( first_name=validated_data['first_name'],last_name=validated_data['last_name'],email=validated_data['email'], username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		Token.objects.create(user=user)
		
		my_redirect_http="https://wnme.herokuapp.com/confirm-email2"

        #send email.
		m = Mailin("https://api.sendinblue.com/v2.0","PpVLAJgjn0mqcW2b")
		to = "mskrdgafie@gmail.com"
		user = "Misiker"
		# print("$$$$$$$$$$$$$$$$$", validated_data['username'])
		data = { "to" : {to:user},
		"from" : ["wnme@gmail.com", "WNME"],"subject" : "confirm your email.",
		"html" : "<h1>Confirm your wnme account</h1><p>Thank you for registering on <h3>WNME<h3>Please confirm your email <a href='" + (my_redirect_http) + "'>here</a></p>"}

		result = m.send_email(data)
		print(result)
		return user
