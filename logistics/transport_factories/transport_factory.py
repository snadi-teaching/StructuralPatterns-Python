from abc import ABC, abstractmethod
from logistics.transport.transport_method import TransportMethod


class TransportFactory(ABC):

    @abstractmethod
    def create(self, identifier: str, capacity_tons: float) -> TransportMethod:
        pass
