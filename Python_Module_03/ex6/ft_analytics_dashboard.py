def list_comprehension(game_data: list):
    """List Comprehension examples generator"""
    try:
        print("\n=== List Comprehension Examples ===")
        high_scorers = [player["name"] for player in game_data
                        if player["score"] > 2000]
        scores_doubled = [player["score"] * 2 for player in game_data]
        active_players = [player["name"] for player in game_data
                          if player["active"]]

        print(f"High scorers (>2000): {high_scorers}")
        print(f"Scores doubled: {scores_doubled}")
        print(f"Active players: {active_players}")

    except Exception:
        print("Error while generating the List Comprehension Examples")


def dict_comprehension_examples(game_data: list):
    """Dict Comprehension Examples generator"""
    print("\n=== Dict Comprehension Examples ===")
    try:
        player_scores = {player["name"]: player["score"]
                         for player in game_data}
        print(f"Player scores: {player_scores}")

        score_categ_lst = [("high" if player["score"] > 2200
                           else "medium" if player["score"] > 2000
                           else "low") for player in game_data]
        score_categ_dict = {categ: score_categ_lst.count(categ)
                            for categ in score_categ_lst}
        print(f"Score categories: {score_categ_dict}")

        achiev_counts = {player["name"]: len(player["achievements"])
                         for player in game_data}
        print(f"Achievement counts: {achiev_counts}")

    except Exception:
        print("Error while generating the Dict Comprehension Examples")


def set_comprehension_examples(game_data: list):
    """Set Comprehension Examples generator"""
    print("\n=== Set Comprehension Examples ===")
    try:
        unique_players = {player["name"] for player in game_data}
        unique_achiev = {ach for player in game_data
                         for ach in player["achievements"]}
        active_reg = {player["region"] for player in game_data}
        print(f"Unique players: {unique_players}")
        print(f"Unique achievements: {unique_achiev}")
        print(f"Active regions: {active_reg}")
    except Exception:
        print("Error while generating the Set Comprehension Examples")


def combined_analysis(game_data: list):
    """Combined Analysis generator"""
    print("\n=== Combined Analysis ===")
    try:
        total_players = len(game_data)
        total_uniq_ach = len({ach for player in game_data
                             for ach in player["achievements"]})
        average_score = sum(player["score"] 
                            for player in game_data) / len(game_data)    
        print(f"Total players: {total_players}")
        print(f"Total unique achievements: {total_uniq_ach}")
        print(f"Average score: {average_score:.1f}")

        top_player_name = ""
        top_player_score = 0
        top_player_achievements = 0
        for player in game_data:
            if player["score"] > top_player_score:
                top_player_score = player["score"]
                top_player_name = player["name"]
                top_player_achievements = len(player["achievements"])
        print(f"Top performer: {top_player_name} "
              f"({top_player_score} points, "
              f"{top_player_achievements} achievements)")
    except Exception:
        print("Error while generating the Combined Analysis")


def ft_analytics_dashboard():
    """Main function to call on the others using the below data"""
    game_data = [
        {
                "name": "alice",
                "score": 2300,
                "region": "north",
                "achievements": ["first_kill", "level_10",
                                 "boss_slayer", "treasure_hunter",
                                 "speed_demon"],
                "active": True
        },
        {
                "name": "bob",
                "score": 1800,
                "region": "east",
                "achievements": ["first_kill", "level_10", "collector"],
                "active": True
        },
        {
                "name": "charlie",
                "score": 2150,
                "region": "north",
                "achievements": ["first_kill", "level_10", "boss_slayer",
                                 "perfectionist", "treasure_hunter",
                                 "speed_demon", "raid_master"],
                "active": True
        },
        {
                "name": "diana",
                "score": 2050,
                "region": "central",
                "achievements": ["first_kill", "level_10"],
                "active": False
        }
    ]
    print("=== Game Analytics Dashboard ===")
    list_comprehension(game_data)
    dict_comprehension_examples(game_data)
    set_comprehension_examples(game_data)
    combined_analysis(game_data)


if __name__ == "__main__":
    ft_analytics_dashboard()
