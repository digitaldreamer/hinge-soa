from django.conf.urls import url
from users.views import (
    UserView,
    UsersView,
)

from urls import ROUTER

ROUTER_URL = 'https://%s/v1/'.format(ROUTER)

urlpatterns = [
    url(r'^users/(?P<uid>[\w-]+)', UserView.as_view()),
    url(r'^users', UsersView.as_view()),
]
