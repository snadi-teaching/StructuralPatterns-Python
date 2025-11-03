from transport.transport_method import TransportMethod


class Ship(TransportMethod):
    def __init__(self, name: str, capacity_tons: float):
        super().__init__(identifier=name, capacity_tons=capacity_tons)

    def transport(self, cargo_weight: float, destination: str):
        if cargo_weight > self.capacity_tons:
            print(f"Error: Cargo exceeds ship capacity of {self.capacity_tons} tons.")
            return
        print(
            f"Ship {self.identifier} transporting {cargo_weight} tons to {destination}."
        )
