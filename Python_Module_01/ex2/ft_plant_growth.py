class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age_days = age

    def get_info(self) -> None:
        """Print the plant information"""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self) -> None:
        """Increase plant height by 1 cm."""
        self.height += 1

    def age(self) -> None:
        """Increase plant age by 1 day."""
        self.age_days += 1


def ft_plant_growth() -> None:
    """Simulate one week of plant growth."""
    curr_day = 1
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    initial_heights = {}
    for plant in plants:
        initial_heights[plant.name] = plant.height
    print(f"=== Day {curr_day} ===")
    for plant in plants:
        plant.get_info()

    while (curr_day < 7):
        for plant in plants:
            plant.grow()
            plant.age()
        curr_day += 1

    print(f"=== Day {curr_day} ===")
    for plant in plants:
        plant.get_info()

    print('\nGrowth this week:')
    for plant in plants:
        growth = plant.height - initial_heights[plant.name]
        print(f"{plant.name}: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
