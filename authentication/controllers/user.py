from database.models import User

def get_or_create_user(userinfo):
    try:
        user = User.objects.get(
            sub = userinfo['sub']
        )
    except:
        user = User.objects.create_user(
            username = userinfo['nickname'],
            first_name = userinfo['given_name'],
            last_name = userinfo['family_name'],
            name = userinfo['name'],
            email = userinfo['email'],
            sub = userinfo['sub'],
            sid = userinfo['sid'],
            picture = userinfo['picture'],
            last_update = 'create user',
        )
        user.save()

    return user