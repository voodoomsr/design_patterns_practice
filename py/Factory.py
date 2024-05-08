### GIST
# Extract away the construction logic, and leave a client work with a factory
# abstraction. The result object of the factory creation will be used in
# a known manner because it is known the type of object the factory generates.
### Use when
# The object setup process is complex: When an object needs a lot of setup
# like setting several properties or even several constructors, factories can
# help keep the code more maintainable by encapsulating this setup process.
# The factory knows about what types of objects can be created and how to create them.
# We need to decouple the creation of an object from the object itself:
# The factory can be an interface for creating objects in a superclass,
# but subclasses specify which classes to instantiate.
# The client is relieved from knowing which type of concrete
# class needs to be instantiated. This allows for more loose coupling.
# A class can't anticipate the objects it needs to create.
# A class wants its subclass to decide which object to create.

class Transport:
    def __init__(self):
        self.trips = 0
        self.type = "Generic transport"

    def deliver(self):
        self.trips += 1
        pass


class Truck(Transport):
    def __init__(self):
        super().__init__()
        self.type = "Truck"

    def deliver(self):
        super().deliver()
        print("Delivering by truck")


class Ship(Transport):
    def __init__(self):
        super().__init__()
        self.type = "Ship"

    def deliver(self):
        super().deliver()
        print("Delivering by ship")


class TransportFactory:
    def create_transport(self):
        pass


class TruckFactory(TransportFactory):
    def create_transport(self):
        return Truck()


class ShipFactory(TransportFactory):
    def create_transport(self):
        return Ship()


def logistics(factory):
    transport = factory.create_transport()
    transport.deliver()
    return transport
