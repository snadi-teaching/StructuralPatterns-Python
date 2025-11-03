from transport_factories.transport_factory import TransportFactory
from transport.transport_method import TransportMethod
from transport.ship import Ship


class ShipFactory(TransportFactory):
    def create(self, identifier: str, capacity_tons: float) -> TransportMethod:
        return Ship(name=identifier, capacity_tons=capacity_tons)
