from django.views.generic import TemplateView
from django.http import JsonResponse

from ..controllers import controller_user
from ..serializers import serializer_user

class profile(TemplateView):
    def get(self, request):
        return JsonResponse({
            'message':'working',
            'user': serializer_user.User_Serializer(controller_user.get_user(request.user), many = False).data
        })