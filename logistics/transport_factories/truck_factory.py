from transport_factories.transport_factory import TransportFactory
from transport.transport_method import TransportMethod
from transport.truck import Truck


class TruckFactory(TransportFactory):
    def create(self, identifier: str, capacity_tons: float) -> TransportMethod:
        return Truck(license_plate=identifier, capacity_tons=capacity_tons)
