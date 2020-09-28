from . import models
from rest_framework  import serializers


class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Rating
		fields = (
			'Order',
			'customer',
			'service_provider',
			'rater',
			'rating',
			'comment',
		)
