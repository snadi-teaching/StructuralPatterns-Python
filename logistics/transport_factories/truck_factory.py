from logistics.transport.transport_factory import TransportFactory
from logistics.transport.transport_method import TransportMethod
from logistics.transport.truck import Truck


class TruckFactory(TransportFactory):
    def create_transport_method(
        self, identifier: str, capacity_tons: float
    ) -> TransportMethod:
        return Truck(license_plate=identifier, capacity_tons=capacity_tons)
