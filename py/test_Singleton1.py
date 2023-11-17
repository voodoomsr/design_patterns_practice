from Singleton1 import Singleton

# Test the Singleton class


def test_singleton():
    # Obtain two instances of the Singleton class
    instance1 = Singleton.getInstance()
    instance2 = Singleton.getInstance()

    # Check if the instances are the same
    assert instance1 is instance2, "Instances are not the same"
