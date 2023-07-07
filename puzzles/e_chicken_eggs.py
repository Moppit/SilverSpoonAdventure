from puzzle import Puzzle
import sys
import time
from textwrap import dedent
sys.path.insert(0, './..')

class ChickenEggs(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Collect the chicken eggs"
        self.save_key = "ECE"

    def puzzle(self):
        print(dedent("""
           Tokiwa: Woohoo, chickens! Here's the chicken coop. 
                   ...
                   Hmmm... have you heard of Mancala, per chance?
              """))

        input(dedent("""
         1) Nod
         2) Tilt your head in confusion
         3) Shake head
              """))

        print(dedent("""
           Tokiwa: Hehe, well I've got an idea! Come on, let's play Mancala
                   with these chicken eggs!
              """))

        input("(Press ENTER to continue)")

        # Mancala!
        
        self.stats.update_strength(1)
        self.stats.update_stamina(-1)
        self.stats.print_stats()
        self.completed = True
