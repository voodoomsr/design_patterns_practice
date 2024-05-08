from Factory import logistics, ShipFactory, TruckFactory

import pytest


@pytest.mark.parametrize("destination, transport_type", [('overseas', 'Ship'), ('land', 'Truck')])
def test_logistics(destination, transport_type):
    if destination == 'overseas':
        factory = ShipFactory()
    else:
        factory = TruckFactory()

    transport = logistics(factory)
    assert transport.type == transport_type
    assert transport.trips == 1
