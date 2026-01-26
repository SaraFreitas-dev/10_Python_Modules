def ft_plant_age() -> None:
    plant_age = int(input('Enter plant age in days: '))
    if plant_age > 60:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow.')
