from truck.truck import Truck
from sea.ship import Ship


def main():
    print("=== Logistics Management System v1.0 ===")

    method = input("Select transportation method (truck/ship): ").strip().lower()

    if method == "truck":

        truck = Truck(license_plate="ABC-123", capacity_tons=10.0)

        truck.transport(cargo_weight=8.5, destination="New York")

    elif method == "ship":

        ship = Ship(name="Sea Explorer", capacity_tons=500.0)

        ship.ship(cargo_weight=300.0, destination="London")


if __name__ == "__main__":
    main()
