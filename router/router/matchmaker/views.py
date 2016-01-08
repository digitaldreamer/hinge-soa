import requests

from django.http import JsonResponse
from django.views.generic import View

from matchmaker.urls_v1 import SERVICE_URL


class MatchesView(View):
    def get(self, request, hydrate=False, *args, **kwargs):
        """
        hydrate - return a profile list instead of the match objects

        query parameters:
            uid - filters the matches for the given user
        """
        uri = '%s/matches'.format(SERVICE_URL)
        uid = kwargs.get('uid', '')
        params = {
            'hydrate': hydrate,
        }

        if uid:
            params['uid'] = uid

        response = requests.get(uri, params=params)
        return JsonResponse(response.json())
