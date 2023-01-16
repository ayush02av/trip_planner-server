from django.views.generic import TemplateView
from django.http import JsonResponse

class profile(TemplateView):
    def get(self, request):
        return JsonResponse({
            'message':'working',
            'user': request.user
        })