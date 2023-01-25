from django.views.generic import TemplateView
from django.http import JsonResponse

from ..serializers import serializer_user

class profile(TemplateView):
    def get(self, request):
        return JsonResponse({
            'message':'working',
            'user': serializer_user.User_Serializer(request.user, many = False).data
        })