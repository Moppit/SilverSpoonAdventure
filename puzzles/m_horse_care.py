from puzzle import Puzzle
import sys
sys.path.insert(0, './..')

class HorseCare(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Feed the horses"
        self.save_key = "MHC"

    def puzzle(self):
        self.stats.update_dexterity(1) # TODO: deleteme
        print("New Implementation!")
