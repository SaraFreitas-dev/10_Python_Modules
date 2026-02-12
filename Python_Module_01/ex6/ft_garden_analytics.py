class Plant:
    """Class to perform actions on the garden"""
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self, amount: int) -> None:
        """Grow plant"""
        self.height += amount

    def info_line(self) -> str:
        """Print info"""
        return (f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Plant that can bloom"""
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Make the plant bloom"""
        self.is_blooming = True

    def info_line(self) -> str:
        """Print decision maker"""
        base = super().info_line()
        if self.is_blooming:
            return (f"{base}, {self.color} flowers (blooming)")
        return (f"{base}, {self.color} flowers")


class PrizeFlower(FloweringPlant):
    """Flowers that give prize points"""
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def info_line(self) -> str:
        """Print info"""
        return (f"{super().info_line()}, Prize points: {self.points}")


class GardenManager:
    """Manager class that represents a garden"""
    total_managed = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats(self)
        GardenManager.total_managed += 1

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant on the list"""
        self.plants.append(plant)

    def grow_all(self) -> None:
        """Grows each plant on the list"""
        for plant in self.plants:
            plant.grow(1)
            print(f"{plant.name} grew 1cm")

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list["GardenManager"]:
        """Creates and returns a list of gardens (network)"""
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    def print_report(self) -> None:
        """Print the report"""
        print()
        print(f"=== {self.owner}'s Garden Report ===")
        print('Plants in garden:')
        for plant in self.plants:
            print(plant.info_line())
        print(f"\nPlants added: {self.stats.plants_added()}, "
              f"Total growth: {self.stats.total_growth()}cm")
        regular, flowering, prize = self.stats.type_counts()
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers\n")

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate grow input - Returns false if it's a negative number"""
        return height >= 0

    class GardenStats:
        """Get stats from garden"""
        def __init__(self, manager: "GardenManager") -> None:
            self.manager = manager

        def total_growth(self) -> int:
            """Get the growth value of a plant"""
            amount = 0
            for plant in self.manager.plants:
                amount += plant.height - plant.initial_height
            return (amount)

        def plants_added(self) -> int:
            """Calculate how many plants were added on a garden"""
            amount = 0
            for _ in self.manager.plants:
                amount += 1
            return (amount)

        def type_counts(self) -> tuple[int, int, int]:
            """Count how many plants there is in a garden by type"""
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.manager.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (regular, flowering, prize)

        def score(self) -> int:
            """Calculate the total score for each owner/garden"""
            score = 0
            for plant in self.manager.plants:
                score += plant.height
                if isinstance(plant, FloweringPlant) and plant.is_blooming:
                    score += 15
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            return (score)


def ft_garden_analytics() -> None:
    """Main function, add gardens and info, print output"""
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    rose.bloom()
    sunflower.bloom()

    print("=== Garden Management System Demo ===")
    print()
    alice.add_plant(oak)
    print("Added Oak Tree to Alice's garden")
    alice.add_plant(rose)
    print("Added Rose to Alice's garden")
    alice.add_plant(sunflower)
    print("Added Sunflower to Alice's garden\n")

    print(f"{alice.owner} is helping all plants grow...")
    alice.grow_all()
    alice.print_report()

    print()
    print(f"Height validation test: {GardenManager.validate_height(1)}")
    bob.add_plant(Plant("Cactus", 92))
    print(f"Garden scores - Alice: {alice.stats.score()}, "
          f"Bob: {bob.stats.score()}")
    print(f"Total gardens managed: {GardenManager.total_managed}")


if __name__ == "__main__":
    ft_garden_analytics()
