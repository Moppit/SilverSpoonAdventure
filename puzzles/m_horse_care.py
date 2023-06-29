from puzzle import Puzzle
import sys
from textwrap import dedent
sys.path.insert(0, './..')

class HorseCare(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Feed the horses"
        self.save_key = "MHC"

    def puzzle(self):
        # TODO: add exit option
        print(dedent("""
              Aki: Okay, let's do it! We have four horses to feed. \n
                   Three of them are in good health so we'll feed them \n
                   the regular diet, but last night I checked on Smoke \n
                   and he looked a little sick so we're going to have \n
                   to adjust his diet
              """))
        print(dedent("""
           Aki: Since he's sick, we don't want to overfeed him, \n
                but we need to make sure he gets all his vitamin, \n
                protien, and energy needs for the day. \n
                He needs 500g of protien and 10M cal of energy. \n
                \n
                One pound of hay gives him:\n
                    0.05g protien\n
                    2 M cal energy\n
                    20% daily value vitamins\n
                \n
                One pound of oats gives him:\n
                    0.2g protien\n
                    3 M cal energy\n
                    5% daily value vitamins\n
                \n
           Aki: I'm not great at math, so I'll leave it to you to \n
                figure out how much hay and oats to give Smoke \n
                so that he eats the minimum weight of food, but \n
                still gets enough protien, energy, and vitamins for the day \n
                """))
        hay = None
        oats = None
        while hay != 4.5 or oats != 2:
            try:
                hay = float(input("Pounds Hay >> "))
                oats = float(input("Pounds Oats >> "))
            except:
                print("Aki: I don't know how much hay and/or oats that would be... \n Tell me one more time.")
            if oats < 2:
                print("Aki: I can't follow the math, but it feels like not enough oats to me")
            elif oats > 2:
                print("Aki: I can't follow the math, but it feels like too much oats to me")
            if hay < 4.5:
                print("Aki: I can't follow the math, but it feels like not enough hay to me")
            elif hay > 4.5:
                print("Aki: I can't follow the math, but it feels like too much hay to me")
        print("Aki: Thanks for doing the math for me, that seems about right.\n Let's feed the horses!")
        self.stats.update_strength(1)
        self.completed = True
