from logistics.transport_factories.truck_factory import TruckFactory


def main():
    print("=== Logistics Management System v1.0 ===")

    method = input("Select transportation method (truck/ship): ").strip().lower()

    if method == "truck":
        factory = TruckFactory()
    elif method == "ship":
        factory = ShipFactory()

    vehicle = factory.create_transport_method(
        identifier="TRANS123", capacity_tons=500.0
    )
    vehicle.transport(cargo_weight=300.0, destination="London")


if __name__ == "__main__":
    main()
