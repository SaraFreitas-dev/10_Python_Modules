def unique_achievements(player1: set, player2: set, player3: set) -> None:
    """Check and print unique achievements"""
    unique_ach = player1.union(player2, player3)
    print(f"All unique achievements: {unique_ach}")
    total = 0
    for _ in unique_ach:
        total += 1
    print(f"Total unique achievements: {total}\n")


def rare_achievements(player1: set, player2: set, player3: set) -> None:
    """Check and print rare achievements"""
    rare_player1 = player1.difference(player2.union(player3))
    rare_player2 = player2.difference(player1.union(player3))
    rare_player3 = player3.difference(player1.union(player2))
    rare_ach = rare_player1.union(rare_player2, rare_player3)
    print(f"Rare achievements {rare_ach}\n")


def ft_achievement_tracker() -> None:
    """Show each players achivements and analytics"""
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    unique_achievements(alice, bob, charlie)
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    rare_achievements(alice, bob, charlie)
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
