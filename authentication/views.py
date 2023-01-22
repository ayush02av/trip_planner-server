from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from .controllers import user as user_controller

oauth = OAuth()
oauth.register(
    "auth0",
    client_id = settings.AUTH0_CLIENT_ID,
    client_secret = settings.AUTH0_CLIENT_SECRET,
    client_kwargs = {
        "scope": "openid profile email",
    },
    server_metadata_url = f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token

    user = user_controller.get_or_create_user(token['userinfo'])

    print(user)

    return redirect(request.build_absolute_uri(reverse("handler")))

def logout(request):
    try:
        request.session.clear()
    except:
        pass

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("handler")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
    
def handler(request):
    if 'user' in request.session.keys():
        token = request.session['user']['id_token']
        query = f'token={token}'
    else:
        query = f'logout=true'
        
    return redirect(f'{settings.CLIENT_URL}/handler?{query}')