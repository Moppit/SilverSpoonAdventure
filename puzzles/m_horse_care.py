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
                   to adjust his diet.
              """))
        input("(Press ENTER to continue)")
        print(dedent("""
           Aki: Since he's sick, we don't want to overfeed him, \n
                but we need to make sure he gets all the nutrition \n
                he needs. Generally its good to feed horses at least \n
                10,000 calories, with 500 grams of protien, and \n
                enough vitamins. 
                """))
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: I believe one pound of hay is around 2,000 calories, \n
                    has 5 grams of protien, and has around 20% of the daily \n
                    value of vitamins.
                """))
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: Meanwhile, oats are like a protien shake for horse, \n
                    giving 3,000 calories and 200 grams of protien, but \n
                    only 5 percent of the daily value of vitamins.
                """))
        input("(Press ENTER to continue)")
        print(dedent("""
           Aki: I'm not great at math, so I'll leave it to you to \n
                figure out how much hay and oats to give Smoke. \n
                Our goal is to meet his nutrition needs while feeding \n
                him as little as possible.
                """))
        hay = None
        oats = None
        while hay != 4.5 or oats != 2:
            try:
                hay_lbs, user_quit = self.input_exitable("How many pounds of hay do you feed Smoke?  ")
                if user_quit:
                    return
                hay = float(hay_lbs)
                print("\n")
                oat_lbs, user_quit = self.input_exitable("How many pounds of oats do you feed Smoke?  ")
                if user_quit:
                    return
                oats = float(oat_lbs)
                print("\n")
            except:
                pass
            if hay != 4.5 or oats != 2:
                print("Aki stops you\n")
                print("Aki: I can't follow the math, but something feels off...")
            if oats and oats < 2:
                print("     I don't think it's enough oats and...")
            elif oats and oats > 2:
                print("     I think it's too much oats and...")
            if hay and hay < 4.5:
                print("     I don't think it's enough hay")
            elif hay and hay > 4.5:
                print("     I think it's too much hay")
            elif hay:
                print("     I think the hay is about right")  
            if hay != 4.5 or oats != 2:
                print("Aki: Let's try again!\n")
        print("Aki: Thanks for doing the math for me, that seems about right.\n Let's feed the horses!")
        self.stats.update_strength(1)
        self.completed = True
