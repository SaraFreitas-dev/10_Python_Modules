import sys


def ft_inventory_system_analysis(inventory_dct: dict) -> None:
    """Calculate total items in dict and unique types"""
    print("=== Inventory System Analysis ===")
    total_items = 0
    unique_types = 0
    for k, v in inventory_dct.items():
        unique_types += 1
        total_items += v
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")


def ft_current_inventory(inventory_dct: dict) -> None:
    """Calculate current inventory and percentage of each unit"""
    print("\n=== Current Inventory ===")
    total_units = 0
    for v in inventory_dct.values():
        total_units += v
    for k, v in inventory_dct.items():
        percentage = (v / total_units) * 100
        print(f"{k}: {v} units ({percentage:.1f}%)")


def ft_inventory_statistics(inventory_dct: dict) -> None:
    """Calculate the most and least abundant"""
    print("\n=== Inventory Statistics ===")
    for k in inventory_dct:
        most_k = k
        least_k = k
        most_v = inventory_dct[k]
        least_v = inventory_dct[k]
        break
    for k in inventory_dct:
        if inventory_dct[k] > most_v:
            most_k = k
            most_v = inventory_dct[k]
        if inventory_dct[k] < least_v:
            least_k = k
            least_v = inventory_dct[k]
    print(f"Most abundant: {most_k} ({most_v} units)")
    print(f"Least abundant: {least_k} ({least_v} units)")


def ft_item_categories(inventory_dct: dict) -> None:
    """Calculate high, moderate and scarce items"""
    print("\n=== Item Categories ===")
    filtered_ab = {}
    filtered_mod = {}
    filtered_sc = {}
    for k, v in inventory_dct.items():
        if v > 10:
            filtered_ab.update({k: v})
        elif v > 4:
            filtered_mod.update({k: v})
        else:
            filtered_sc.update({k: v})
    if filtered_ab:
        print(f"Abundant: {filtered_ab}")
    if filtered_mod:
        print(f"Moderate: {filtered_mod}")
    if filtered_sc:
        print(f"Scarce: {filtered_sc}")


def ft_management_suggestions(inventory_dct: dict) -> None:
    """Check what items are low on stock"""
    print("\n=== Management Suggestions ===")
    restock_items = []
    for k, v in inventory_dct.items():
        if v < 2:
            restock_items.append(k)
    print(f"Restock needed: {restock_items}")


def ft_dictionary_properties_demo(inventory_dct: dict) -> None:
    """Show keys, values and a lookup item example"""
    print("\n=== Dictionary Properties Demo ===")
    dict_keys = []
    dict_values = []
    for k, v in inventory_dct.items():
        dict_keys.append(k)
        dict_values.append(v)
    print(f"Dictionary keys: {dict_keys}")
    print(f"Dictionary values: {dict_values}")
    if 'sword' in inventory_dct:
        print("Sample lookup - 'sword' in inventory: True")
    else:
        print("Sample lookup - 'sword' in inventory: False")


def ft_inventory_system() -> None:
    """Main function"""
    inventory = {}
    i = 1
    while i < len(sys.argv):
        item = sys.argv[i].split(":")
        name = item[0]
        quantity = int(item[1])
        inventory.update({name: quantity})
        i += 1
    if not inventory:
        print("No items to analyze.")
        return
    ft_inventory_system_analysis(inventory)
    ft_current_inventory(inventory)
    ft_inventory_statistics(inventory)
    ft_item_categories(inventory)
    ft_management_suggestions(inventory)
    ft_dictionary_properties_demo(inventory)


if __name__ == "__main__":
    ft_inventory_system()
