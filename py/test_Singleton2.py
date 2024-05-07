import pytest
from Singleton2 import Singleton


@pytest.fixture(autouse=True)
def reset_singleton():
    Singleton._instance = None


def test_singleton_instance():
    # Create two instances of Singleton
    instance1 = Singleton()
    instance2 = Singleton()

    # Check if both instances are the same
    assert instance1 is instance2


def test_singleton_data():
    # Create an instance of Singleton with data
    data = "Hello, World!"
    instance = Singleton(data)

    # Check if the data is stored correctly in the instance
    assert instance.data == data


def test_singleton_modify_data():
    # Create an instance of Singleton with data
    data = "Hello, World!"
    instance = Singleton(data)

    # Modify the data in the instance
    new_data = "Modified data"
    instance.data = new_data

    # Create a new instance of Singleton
    new_instance = Singleton()

    # Check if the new instance has the modified data
    assert new_instance.data == new_data
