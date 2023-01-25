import jwt
from django.http import JsonResponse
from ..controllers.controller_user import get_user

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'path') and 'api' in request.path:
            if 'Authorization' not in request.headers.keys():
                return JsonResponse({
                    'message':'not logged in'
                })
            
            token = request.headers['Authorization'].split()[1]
            decoded = jwt.decode(token, options={"verify_signature": False})

            request.user = get_user(decoded)

        response = self.get_response(request)

        return response