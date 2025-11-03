from logistics.transport.transport_method import TransportMethod


class Truck(TransportMethod):
    def __init__(self, license_plate: str, capacity_tons: float):
        super().__init__(identifier=license_plate, capacity_tons=capacity_tons)

    def transport(self, cargo_weight: float, destination: str):
        if cargo_weight > self.capacity_tons:
            print(f"Error: Cargo exceeds truck capacity of {self.capacity_tons} tons.")
            return
        print(
            f"Truck {self.identifier} transporting {cargo_weight} tons to {destination}."
        )
