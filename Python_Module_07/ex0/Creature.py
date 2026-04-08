from abc import ABC, abstractmethod

class Creature(ABC):
    """Abstract class used for all creature types"""
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self, attacker: str) -> str:
        pass

    def describe(self) -> str:
        return (f'{self.name} is a {self.type} type Creature')
