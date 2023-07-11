from puzzle import Puzzle
import sys
from textwrap import dedent
from PIL import Image
sys.path.insert(0, './..')

class Lunch(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Make pizza for lunch"
        self.save_key = "ALU"

    def puzzle(self):
        # Puzzle intro
        print(dedent("""
         Hachiken: Lunch it is! I've been doing a bit of research, and I think I'm ready
                   to make the perfect pizza that will cater to each person's desire. Can
                   you help me work out the final configuration? 
              """))
        input(dedent("""
                1) Yes!!
                2) Sure thing!
                3) 🍕
                    """))

        print(dedent("""
                Hachiken: Thanks! So here's what I have so far.
                    """))

        input("(Press ENTER to continue)")

        # Display puzzle
        img = Image.open("res/lunch_puzzle.jpg")
        img.show()
        
        # Start puzzle
        print(dedent(f"""
         Hachiken: I did a poll a while back to figure out people's topping preferences.
                   Each person provided 3 critical topping preferences, and the rest are
                   somewhat flexible, so we can figure out the rest. In order to make the
                   pizza aesthetically pleasing: 
                   
                   1) No two toppings can appear at two different spots at the same distance 
                      from the center.
                   2) I want to make sure everyone tries each topping, so they have to have
                      every topping on each slice.
                   3) The poll ranked 8 toppings, with 1 as least favorite and 8 as favorite.
              """))
        input("(Press ENTER to continue)")

        print(dedent("""
            Hachiken: Let's just figure out Komaba's slice for now, since he'll need it soon.
        """))
        input("(Press ENTER to continue)")

        guess = None
        answer = 'OBMHAPST'
        while guess != answer:
            try:
                print("Which toppings does Komaba want, ordered from 1-8?")
                guess, user_quit = self.input_exitable("Enter the first letter of each topping, all caps and no spaces (or type 'q' to quit) >> ")
                if user_quit:
                    return
            except:
                pass
            if guess != answer:
                print("\nHachiken stops you")
                print("Hachiken: My memory's foggy, but I don't think Komaba has topped his pizza that way.")
                print("          Let's try again!")
        
        print(dedent("""
       Hachiken: Oooh, thanks for topping his slice! This kind of makes sense to me now. Let me do the rest,
                 and then we can put the pizza in the oven! It should be done by lunchtime.
              """))
        self.stats.update_strength(1)
        self.stats.update_stamina(-1)
        self.stats.print_stats()
        self.completed = True