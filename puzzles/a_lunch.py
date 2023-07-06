from puzzle import Puzzle
import sys
from textwrap import dedent
from PIL import Image
sys.path.insert(0, './..')

class Lunch(Puzzle):

    def __init__(self, stats, completed=False, komaba_visited=False):
        super().__init__(stats, completed)
        self.description = "Make lunch"
        self.save_key = "ALU"
        self.komaba_visited = komaba_visited

    def puzzle(self):
        # TODO: add exit option

        # Puzzle intro
        print(dedent("""
         Hachiken: Lunch it is! Fair warning, all of these guys are\n
                   *super* picky about their food. We're going to make\n
                   pizza today, here's the recipe.
              """))
        input("(Press ENTER to continue)")

        # Display puzzle
        img = Image.open("res/lunch_puzzle.jpg")
        img.show()
        
        # Start puzzle
        follow_up_dialogue = None
        if self.komaba_visited:
            follow_up_dialogue = "he's waiting on his slice"
        else:
            follow_up_dialogue = "I have a feeling he'll stop by soon"

        print(dedent(f"""
         Hachiken: It's super cryptic, so I'm not sure what to do. All I know is that
                   each person wants all of the toppings, and they don't want anyone
                   else to have the same topping as them per circular ring. Do you think
                   you can figure it out? Let's just figure out Komaba's slice for now,
                   since {follow_up_dialogue}.
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
                 and then we can put the pizza in the oven!
              """))
        self.stats.update_stamina(-1)
        self.stats.print_stats()
        self.completed = True