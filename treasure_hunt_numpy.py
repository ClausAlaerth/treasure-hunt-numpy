import numpy as np


# Color class
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


original_map = np.random.randint(1, 10, size=(5, 5))

# Treasure position must not be at (0, 0)
while True:
    treasure_row, treasure_col = np.random.randint(0, 5, size=2)

    if (treasure_row, treasure_col) != (0, 0):
        break

player_position = (0, 0)
score = 0


def print_map(original_map, player_position):
    player_map = original_map.copy()
    player_row, player_col = player_position
    player_map[player_row, player_col] = -1

    player_map_str = player_map.astype(str)  # String conversion for display
    player_map_str[player_map_str == "-1"] = Color.OKGREEN + "P" + Color.ENDC

    print("\nCurrent Map:\n")
    for row in player_map_str:
        print(" ".join(row))


# Main loop
while True:
    print_map(original_map, player_position)

    direction = input(
        "\nEnter direction (w/a/s/d) or 'q' to quit: ").strip().lower()

    movement = {
        "w": (-1, 0),  # Up
        "a": (0, -1),  # Left
        "s": (1, 0),  # Down
        "d": (0, 1)   # Right
    }
    if direction == "q":
        print(Color.OKGREEN + "\nThanks for playing!\n" + Color.ENDC)
        break

    elif direction in movement:
        new_position = (
            player_position[0] + movement[direction][0],
            player_position[1] + movement[direction][1]
        )

    else:
        print(Color.FAIL + "\nInvalid direction!" +
              Color.ENDC + " Please use (w/a/s/d) or 'q'.")
        continue

    # Check boundaries
    if not (0 <= new_position[0] < original_map.shape[0] and
            0 <= new_position[1] < original_map.shape[1]):
        print(Color.FAIL + "\nOut of bounds!" + Color.ENDC + " Try again.")
        continue

    player_position = new_position
    score += 1

    # Check for treasure
    if player_position == (treasure_row, treasure_col):
        print(Color.OKGREEN + "\nCongratulations!" + Color.ENDC)
        print(f"You found the treasure at {player_position}!")
        print(f"Your score is: {score}\n")
        break
