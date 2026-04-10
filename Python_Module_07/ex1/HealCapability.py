from abc import ABC, abstractmethod


class HealCapability(ABC):
    """To give a heal capability"""
    @abstractmethod
    def heal(self) -> str:
        """Define the heal abstract method. The target is optional"""
        pass
