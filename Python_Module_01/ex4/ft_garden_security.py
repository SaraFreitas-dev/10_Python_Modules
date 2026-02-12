class SecurePlant:
    def __init__(self, name: str) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        """Returns plant height"""
        return self.__height

    def get_age(self) -> int:
        """Returns plant age"""
        return self.__age

    def set_height(self, height: int) -> None:
        """Sets plant height"""
        if height < 0:
            print(f'Invalid operation attempted: height {height}cm [REJECTED]')
            print('Security: Negative height rejected')
        else:
            self.__height = height
            print(f'Height updated: {height}cm [OK]')

    def set_age(self, age: int) -> None:
        """Sets plant age"""
        if age < 0:
            print(f'Invalid operation attempted: age {age} days [REJECTED]')
            print('Security: Negative age rejected')
        else:
            self.__age = age
            print(f'Age updated: {age} days [OK]')

    def get_info(self) -> None:
        """Print plant info"""
        print()
        print(f"Current plant: {self.name} "
              f"({self.__height}cm, {self.__age} days)")


def ft_garden_security() -> None:
    """main function"""
    print('=== Garden Security System ===')
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
