from django.conf.urls import url
from matches.views import (
    MatchesView,
)

from urls import ROUTER

ROUTER_URL = 'https://%s/v1/'.format(ROUTER)

urlpatterns = [
    url(r'^matches', MatchesView.as_view()),
]
