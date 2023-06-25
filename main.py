from stats import Stats
from puzzles.m_horse_care import HorseCare
from puzzle_set import PuzzleSet

# Stats tracking vars
# Instantiated here, read from file
stats = Stats()

# Welcome code

# Puzzle Set 1 - Morning
    # Update the global stats object
horse_care = HorseCare(stats, False)
morning = PuzzleSet(stats, [horse_care,horse_care,horse_care])
if not morning.set_complete:
    stats = morning.run()

# Puzzle - Horse Riding Event
horse_riding_puzzle_complete = True # TODO: make actual obj
if morning.set_complete and not horse_riding_puzzle_complete:
    print("TODO")

# Puzzle Set 2 - Afternoon
afternoon = PuzzleSet(stats, [horse_care,horse_care,horse_care])
if horse_riding_puzzle_complete and not afternoon.set_complete:
    print("TODO")

# Puzzle - Baseball

# Puzzle Set 3 - Evening

# Talk with Komaba

# Wrap Up

# Save and exit
print("Game has been saved.")
# TODO: write to the file here