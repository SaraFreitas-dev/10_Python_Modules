def ft_count_harvest_iterative() -> None:
    total_days = int(input('Days until harvest: '))
    days_range = range(1, (total_days + 1))
    for n in days_range:
        print(f'Day {n}')
    print('Harvest time!')
