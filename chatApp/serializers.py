from . import models
from rest_framework  import serializers


class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Chat
		fields = (
			'service_provider',
			'customer',
			'sender',
			'text',
		)