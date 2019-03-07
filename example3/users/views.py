
from django.http import JsonResponse
from .services import TAS
from django.contrib.auth.models import User

def get_user_info(request, userId):
    """
    This route looks up a user in the database given their ID,
    calls the TAS service and returns the users info from TAS
    :param request:
    :param userId:
    :return:
    """
    print(userId)
    user = User.objects.get(pk=userId)

    #create our TAS client
    client = TAS("SECRETKEY")

    #get the user info from the TAS service
    info = client.getUserInfo(user.username)

    return JsonResponse(info)