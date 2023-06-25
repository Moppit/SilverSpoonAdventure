# Template for each of the individual puzzles
# Make a subclass of this for your puzzle
# TODO: naming convention?
import puzzle_utils

class Puzzle:

    def __init__(self, stats, completed=False):
        self.stats = stats
        self.description = None
        self.save_key = None
        self.completed = completed
        # self.util = puzzle_utils (make a class)

    def run(self):
        self.puzzle()
        return self.stats

    # ===== DON'T FORGET!!!!! =====
    # Make sure to update the stats object!
    # Make sure to always set the puzzle completion status!
    # And always make sure there's a way to exit! (last option)
    # =============================
    def puzzle(self):
        pass