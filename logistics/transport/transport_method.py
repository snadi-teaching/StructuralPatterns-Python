from abc import ABC, abstractmethod


class TransportMethod(ABC):
    def __init__(self, identifier: str, capacity_tons: float):
        self.identifier = identifier
        self.capacity_tons = capacity_tons

    @abstractmethod
    def transport(self, cargo_weight: float, destination: str):
        pass
