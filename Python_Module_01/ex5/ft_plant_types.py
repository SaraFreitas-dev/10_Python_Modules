class Plant:
    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def get_basic_info(self) -> str:
        """Print Basics"""
        return (f"{self.name} ({self.kind}): "
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        """Initialize a Plant Subclass"""
        self.color = color
        self.kind = "Flower"

    def bloom(self) -> None:
        print(f'{self.name} is blooming beautifully!\n')

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        """Initialize a Plant Subclass"""
        self.trunk_diameter = trunk_diameter
        self.kind = "Tree"

    def produce_shade(self) -> None:
        print(f'{self.name} provides {int(3.14 * self.trunk_diameter ** 2)} '
              f'square meters of shade\n')

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}, {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        """Initialize a Plant Subclass"""
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.kind = "Vegetable"

    def nut_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}, {self.harvest_season} harvest")
        self.nut_value()


def ft_plant_types() -> None:
    """Main Function"""
    garden = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 15, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1500, 40),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 60, "spring", "vitamin A")
    ]

    print('=== Garden Plant Types ===')
    for plant in garden:
        plant.get_info()


if __name__ == "__main__":
    ft_plant_types()
