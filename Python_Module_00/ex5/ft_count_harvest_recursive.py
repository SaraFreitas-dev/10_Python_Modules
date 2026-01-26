def count(day: int, total_days: int) -> None:
    if day > total_days:
        print('Harvest time!')
        return
    print(f'Day {day}')
    count((day + 1), total_days)


def ft_count_harvest_recursive() -> None:
    total_days = int(input('Days until harvest: '))
    count(1, total_days)
