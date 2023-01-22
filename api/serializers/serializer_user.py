from rest_framework import serializers
from database.models import User

class User_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = User
		exclude = (
			'password',
			'is_active',
			'is_staff',
			'is_superuser',
			'user_permissions'
		)