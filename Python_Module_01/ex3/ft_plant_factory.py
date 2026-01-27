class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age_days = age

    def get_info(self):
        """Print all info for each plant"""
        print(f"Created: {self.name} ({self.height}cm, {self.age_days} days)")


def ft_plant_factory() -> None:
    """main function"""
    total_created = 0
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    print('=== Plant Factory Output ===')
    for plant in plants:
        plant.get_info()
        total_created += 1
    print(f'\nTotal plants created: {total_created}')


if __name__ == "__main__":
    ft_plant_factory()
