# Settings for each difficulty level
# used to configure the game state at start

LEVELS = {
    "EASY": {
        "spawn_interval": 180,  # 3 Seconds between packages
        "score_threshold": 50,  # Score needed to increase package count
        "miss_removal_rate": 3, # Every 3 trucks, remove 1 miss
        "crazy_controls": False, # Normal controls
        "speeds": {0: 1, "even": 1, "odd": 1} # Standard 1x speed
    },
    "MEDIUM": {
        "spawn_interval": 120,  # Faster spawn (2s)
        "score_threshold": 30,
        "miss_removal_rate": 5,
        "crazy_controls": False,
        "speeds": {0: 1, "even": 1, "odd": 1.5} # Odd floors move 1.5x faster
    },
    "EXTREME": {
        "spawn_interval": 90,   # Very fast spawn (1.5s)
        "score_threshold": 30,
        "miss_removal_rate": 5,
        "crazy_controls": False,
        "speeds": {0: 1, "even": 1.5, "odd": 2.0} # Fast mixing speeds
    },
    "CRAZY": {
        "spawn_interval": 60,   # Chaos mode (1s)
        "score_threshold": 20,
        "miss_removal_rate": None, # Misses are never removed
        "crazy_controls": True, # Controls are inverted!
        "speeds": {0: 1, "even": "random", "odd": "random"} # Random speeds
    }
}

def get_difficulty(level_name):
    """Safely retrieves the dictionary for a level name."""
    # Defaults to EASY if the name is not found
    return LEVELS.get(level_name, LEVELS["EASY"])