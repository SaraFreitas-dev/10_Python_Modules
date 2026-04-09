from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """To give a transform capability"""
    @abstractmethod
    def transform(self) -> str:
        """Transform the creature for a short period"""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Reverse the creature back to its first level form"""
        pass
