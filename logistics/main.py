from transport_factories.truck_factory import TransportFactory
from transport_factories.ship_factory import ShipFactory
from transport_factories.truck_factory import TruckFactory


def main():
    print("=== Logistics Management System v1.0 ===")

    factory = get_factory()
    start_transport(factory)


def start_transport(factory: TransportFactory):
    vehicle = factory.create(identifier="TRANS123", capacity_tons=500.0)
    vehicle.transport(cargo_weight=300.0, destination="London")


def get_factory():
    method = input("Select transportation method (truck/ship): ").strip().lower()

    if method == "truck":
        return TruckFactory()
    elif method == "ship":
        return ShipFactory()


if __name__ == "__main__":
    main()
