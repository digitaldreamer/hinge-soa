from django.conf.urls import url
from matchmaker.views import (
    MatchesView,
)

from urls import SERVICE_MAP

SERVICE = 'matchmaker'
SERVICE_URL = 'https://%s/v1/'.format(SERVICE_MAP[SERVICE])

urlpatterns = [
    url(r'^matches', MatchesView.as_view()),
    url(r'^users/(?P<uid>[\w-]+)/matches', MatchesView.as_view(hydrate=True)),
]
