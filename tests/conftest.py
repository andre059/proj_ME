import pytest


@pytest.fixture
def entering_data():
    return [10000, 20]


@pytest.fixture
def changing_discount():
    return [10000, 0.8]
