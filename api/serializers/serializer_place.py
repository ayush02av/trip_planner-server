from rest_framework import serializers
from database.models import Place

class Place_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = Place
		exclude = ('users',)