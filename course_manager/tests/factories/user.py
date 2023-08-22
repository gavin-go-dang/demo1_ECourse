from django.test import TestCase, Client
from authen.models import User
from factory.django import DjangoModelFactory
from django.contrib.auth.hashers import make_password
from factory import LazyFunction
import factory
from faker import Faker


fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_staff = True
    is_superuser = True
