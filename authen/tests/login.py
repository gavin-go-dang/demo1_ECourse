from django.contrib.auth import authenticate, login
from django.test import Client


def create_logged_in_user(client, user):
    if not isinstance(client, Client):
        client = Client()

    authenticated_user = authenticate(username=user.username, password="your_password")

    if authenticated_user:
        login(client, user=authenticated_user)

    return client
