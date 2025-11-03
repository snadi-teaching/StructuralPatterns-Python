from logistics.transport.transport_factory import TransportFactory
from logistics.transport.transport_method import TransportMethod
from logistics.transport.ship import Ship


class ShipFactory(TransportFactory):
    def create_transport_method(
        self, identifier: str, capacity_tons: float
    ) -> TransportMethod:
        return Ship(name=identifier, capacity_tons=capacity_tons)
