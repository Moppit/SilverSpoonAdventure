from puzzle import Puzzle
import sys
from textwrap import dedent
from PIL import Image
import time
sys.path.insert(0, './..')

class PigPen(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Fix the pig pen"
        self.save_key = "APP"

    def puzzle(self):
        print(dedent("""
              Hachiken: Here is the pig pen. I like to come here everyday to feed these guys and check
                        out how they're doing.
              """))
        input("(Press ENTER to continue)")
        print(dedent("""
              Hachiken: Ahh... Nice! It looks like Nem Lui and Bún Chả have finally grown a bit
                        they should be fine pigs when they grow up. It also looks like Gyoza's
                        almost fully grown. It will be sad to see him go, but I'm sure he'll be
                        delicious. I raised him well!
              """))
        input("(Press ENTER to continue)")
        print(dedent("""
              Hachiken: Unfortunately, it looks like the pig pen is in need of repair. I'll gather
                        the pigs. Meanwhile, can I let you plan out the the layout of the stalls?
              """))
        _, user_exit = self.input_exitable("1. Sure\n2. I'll do my best\n3. 🐷\n>> ")
        if user_exit:
            return
        print(dedent("""
              Hachiken: Awesome! Each pig needs its own stall and to simplify the construction a
                        bit let's make all the stalls rectangular. Older pigs will also need more
                        room than the younger pigs, let's say they need one square foot when they're
                        born and one additional square foot for each month that they have lived. So
                        for example, Gyoza will need 6 square feet of room in his stall. Finally, we
                        don't want to waste any space, so make sure you use all of the available room.
              """))
        input("(Press ENTER to continue)")
        print(dedent("""
              Hachiken hands you a map of the stall to fill out along with a chart of the ages of 
              the pigs.
              """))
        # Show drawing
        img = Image.open("res/pig_pen_1.png")
        img.show()
        img = Image.open("res/pig_age_chart_1.png")
        img.show()
        
    
            
        pig = None
        while pig != "chashu":
            pig, user_quit = self.input_exitable("\nFind out how divide the pig pen into stalls, then enter the name of the pig who gets\nthe marked square: ")
            if user_quit:
                return
            pig = pig.lower()
            if pig != "chashu":
                print("\nHachiken: I don't think that will work. Try moving some walls around.")
        
        print("\nHachiken: That layout looks good. Let's setup the walls and put the pigs in.\n")
        input("(Press ENTER to continue)")
        print("\nAfter a lot of hammering and chasing around pigs, you and Hachiken get the pen set up.\n")
        input("(Press ENTER to continue)")
        print("\nHachiken: Looks good as new! Nice work!\n")
        input("(Press ENTER to continue)")
        print()
        self.stats.update_strength(1)
        self.stats.update_dexterity(1)
        self.stats.update_stamina(-2)
        self.stats.print_stats()
        input("\n(Press ENTER to continue)")
        self.completed = True
