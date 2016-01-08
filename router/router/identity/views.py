import requests

from django.http import JsonResponse
from django.views.generic import View

from identity.urls_v1 import SERVICE_URL


class UserView(View):
    def get(self, request, uid, *args, **kwargs):
        uri = '%s/users/%s'.format(SERVICE_URL, uid)
        response = requests.get(uri)
        return JsonResponse(response.json())


class UsersView(View):
    def get(self, request, *args, **kwargs):
        uri = '%s/users'.format(SERVICE_URL)
        uids = request.GET.get('uids')
        params = {
            'uids': uids,
        }
        response = requests.get(uri, params=params)
        return JsonResponse(response.json())
