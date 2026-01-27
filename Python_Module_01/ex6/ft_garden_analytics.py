class GardenManager:
    """Manager class that represents a garden"""
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant) -> None:
        """Adds a plant on the list"""
        self.plants.append(plant)

    def grow_all(self) -> None:
        """Grows each plant on the list"""
        for plant in self.plants:
            plant.grow(1)

    @classmethod
    def create_garden_network(cls) -> list:
        """Creates and returns a list of gardens (network)"""
        return [cls("Alice"), cls("Bob")]

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate grow input - Returns false if it's a negative number"""
        return height >= 0


class Plant:
    """Class to perform actions on the garden"""
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        self.height += amount

    def get_basic_info(self) -> str:
        return (f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Plant that can bloom"""
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Make the plant bloom"""
        self.is_blooming = True

    def info_line(self) -> str:
        """If else print"""
        if self.is_blooming:
            return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)"
        return f"- {self.name}: {self.height}cm, {self.color} flowers"

    def get_info(self) -> None:
        """Call print function"""
        print(self.info_line())


class PrizeFlower(FloweringPlant):
    """Flowers that give prize points"""
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points
        
    def get_info(self) -> None:
        """Print info"""
        print(f"{self.info_line()}, Prize points: {self.points}")

