import requests

from django.http import JsonResponse
from django.views.generic import View

from matches.models import Match
from matches.urls_v1 import ROUTER_URL


class MatchesView(View):
    def get(self, request, *args, **kwargs):
        """
        this has an optional `uid` query parameter that filters the matches for the given user
        """
        uid = kwargs.get('uid', '')
        hydrate = request.GET.get('hydrate', False)
        match_list = Match.get_matches(uid=uid, state='match')
        response_json = []

        if uid and hydrate:
            response_json = self._hydrate_match_list(uid, match_list)
        else:
            response_json = [match.json() for match in match_list]

        return JsonResponse(response_json)

    def _hydrate_match_list(self, player_uid, match_list):
        """
        takes the match_list and returns a hydrated list of matched users for the player_uid
        """
        user_list = [match.subject_uid(player_uid) for match in match_list]

        uri = '%s/users'.format(ROUTER_URL)
        params = {
            'uids': user_list,
        }
        response = request.get(uri, params=params)
        return response.json()
