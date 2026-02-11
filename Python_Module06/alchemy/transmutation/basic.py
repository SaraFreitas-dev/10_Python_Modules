from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmuted to gold"""
    return (f"Lead transmuted to gold using {create_fire()}")


def stone_to_gem() -> str:
    """Transmuted to gem"""
    return (f"Stone transmuted to gem using {create_earth()}")
