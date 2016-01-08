from django.conf.urls import url
from identity.views import (
    UsersView,
    UserView,
)

from urls import SERVICE_MAP

SERVICE = 'identity'
SERVICE_URL = 'https://%s/v1/'.format(SERVICE_MAP[SERVICE])

urlpatterns = [
    url(r'^users', UsersView.as_view()),
    url(r'^users/(?P<user_id>[\w-]+)', UserView.as_view()),
]
