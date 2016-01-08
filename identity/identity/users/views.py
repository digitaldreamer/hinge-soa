import requests

from django.http import JsonResponse
from django.views.generic import View

from users.models import User
from users.urls_v1 import ROUTER_URL


class UserView(View):
    pass

class UsersView(View):
    def get(self, request, *args, **kwargs):
        """
        return a set of users

        query params:
            uids - list of uids
        """
        uids = request.GET.get('uids', [])
        users = User.get_users_by_uids(uids)
        response_json = [user.json() for user in users]
        return JsonResponse(response_json)
