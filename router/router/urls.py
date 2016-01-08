"""router URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

SERVICE_MAP = {
    'identity': 'api.hinge.co:8001',
    'matchmaker': 'api.hinge.co:8002',
}

urlpatterns = [
    url(r'^v1/', include('identity.urls_v1')),
    url(r'^v1/', include('matches.urls_v1')),
]
