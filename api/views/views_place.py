from django.views.generic import TemplateView
from django.http import JsonResponse
import json

from ..serializers import serializer_place

class place(TemplateView):
    def get(self, request):
        serializer = serializer_place.Place_Serializer(serializer_place.Place.objects.filter(admin = request.user.id), many = True)

        return JsonResponse({
            'message': 'Places fetched',
            'data': serializer.data
        })
    
    def post(self, request):
        data = json.loads(request.body.decode('utf8'))
        data['admin'] = request.user.id
        
        serializer = serializer_place.Place_Serializer(data = data)
        
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({
                'message': 'new place added'
            })
        else:
            print(serializer.data)
            print(serializer.errors)
            return JsonResponse({
                'message': 'error'
            })