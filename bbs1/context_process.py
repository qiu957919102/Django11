from .models import User


def bbs1_user(request):
    user_id = request.session.get('user_id')
    context = {}

    if user_id:
        try:
            user_info = User.objects.get(pk=user_id)
            context['user_info'] = user_info
        except:
            pass
    return context