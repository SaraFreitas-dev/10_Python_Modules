class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        """Print the plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """Create and display a registry of garden plants."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.print_info()


if __name__ == "__main__":
    ft_garden_data()
