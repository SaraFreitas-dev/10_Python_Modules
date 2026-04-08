from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract class used for all creature types"""
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        """Str to describe the type of attack that a creature has"""
        pass

    def describe(self) -> str:
        """Str to describe a creature"""
        return (f'{self.name} is a {self.type} type Creature')
