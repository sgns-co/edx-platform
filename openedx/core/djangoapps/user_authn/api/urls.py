"""
Logistration API urls
"""

from django.conf.urls import url

from openedx.core.djangoapps.user_authn.api.views import ThirdPartyAuthContext

urlpatterns = [
    url(
        r'^third_party_auth_context$', ThirdPartyAuthContext.as_view(), name='third_party_auth_context'
    ),
]
