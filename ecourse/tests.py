from django.conf import settings

settings.STATICFILES_STORAGE = "your_app.storages.StaticStorage"
settings.DEFAULT_FILE_STORAGE = "your_app.storages.PublicMediaStorage"

import pytest
from django.core.files.storage import default_storage
from ecourse.storage_backends import StaticStorage


@pytest.fixture
def static_storage():
    return StaticStorage()


def test_static_storage(static_storage):
    assert isinstance(static_storage, StaticStorage)

    assert static_storage.location == "static"

    assert static_storage.default_acl == "public-read"

    with default_storage.open("test_file.txt", "w") as f:
        f.write("Test content")

    assert default_storage.exists("test_file.txt")

    url = default_storage.url("test_file.txt")
    assert "public-read" in url
