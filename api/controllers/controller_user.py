from database.models import User

def get_user(userinfo):
    user = User.objects.get(
        sub = userinfo['sub']
    )

    return user