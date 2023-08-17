from django.conf import settings

# Sử dụng S3 cho static và media files trong unit test
settings.STATICFILES_STORAGE = "your_app.storages.StaticStorage"
settings.DEFAULT_FILE_STORAGE = "your_app.storages.PublicMediaStorage"

import pytest
from django.core.files.storage import default_storage
from ecourse.storage_backends import StaticStorage


@pytest.fixture
def static_storage():
    return StaticStorage()


def test_static_storage(static_storage):
    # Kiểm tra xem storage backend là `StaticStorage`
    assert isinstance(static_storage, StaticStorage)

    # Kiểm tra location của storage
    assert static_storage.location == "static"

    # Kiểm tra default_acl của storage
    assert static_storage.default_acl == "public-read"

    # Tạo một file tạm thời và lưu nó vào storage
    with default_storage.open("test_file.txt", "w") as f:
        f.write("Test content")

    # Kiểm tra xem file đã được lưu vào storage chưa
    assert default_storage.exists("test_file.txt")

    # Kiểm tra xem file có quyền public-read chưa
    url = default_storage.url("test_file.txt")
    assert "public-read" in url
