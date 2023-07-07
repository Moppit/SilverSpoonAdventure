from puzzle import Puzzle
import sys
from textwrap import dedent
from PIL import Image
import time
import string
sys.path.insert(0, './..')

class HorseRide(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Ride a horse"
        self.save_key = "MHR"

    def puzzle(self):
        # TODO: add exit option
        print(dedent("""
              Aki: Now that we've taken care of all the horse chores, do you want to go for a horse
                   ride around the practice track?
              """))
        _, user_exit = self.input_exitable(">> ")
        if user_exit:
            return
        print(dedent("""
           Aki: Great! Why don't you ride Kemuri? Kemuri's really nice and pretty even tempered, so he's
                great for a first timer like you. 
           """))
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki hands you a brush and leads you over to Kemuri's pen.
                """))
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: First we want to brush his hair. This will help you get to know one another before
                    you start riding him. While you're brushing, you want to pay special attention to
                    where the saddle goes. A small burr in this area can turn into a wound after riding.
                """))
        input("(Press ENTER to continue)")
        print("\nYou brush Kemuri's hair according to the instructions\n")
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: Now we want to check the hooves to make sure the horseshoes are fitting properly and
                    there is no rocks stuck in the hooves. You can use this tool to remove any debris.
                """))
        input("(Press ENTER to continue)")
        print("\nAki hands you a hook shaped tool.\n")
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: It can be a bit challenging to get horses to pick up their hooves, so take your
                    time and let Kemuri know what you are doing by tapping his leg with your hands. 
                """))
        input("(Press ENTER to continue)")
        stat_check = None
        while(True):
            print("\nRoll a d20 for dexterity to see how well you do at picking up and cleaning the hooves.")
            roll, user_quit = self.input_exitable("Enter result >> ")
            if user_quit:
                return
            try:
                stat_check = int(roll.strip()) + self.stats.dexterity
                break
            except:
                print("Enter an integer")
        if stat_check < 10:
            print(dedent("""
            Dexterity Check less than 10: You pull on the right hind hoof with all your might,
                                          but it won't budge. Kemuri get's annoyed and you have
                                          to jump back right before he kicks the place you were
                                          just standing in.
            """))
            input("(Press ENTER to continue)")
            print(dedent("""
               Aki: Ohhh... Sorry! Usually Kemuri's calmer than that. Let me take care of it.
                """))
            input("(Press ENTER to continue)")
            print("\nAki slowly approaches Kemuri and gently scratches his nose. When he seems\nto have calmed down, she picks up the hooves one at a time and cleans them.\n")
        elif stat_check < 20:
            print(dedent("""
            Dexterity Check between 10-19: You easily lift Kemuri's front hooves one by one and clean them.
                                           However, when you try to lift the back hooves, Kemuri refuses to
                                           let you lift them, no matter how hard you try.
            """))
            input("(Press ENTER to continue)")
            print("\nAki: The back hooves can be a bit tricky let me help.")
            input("\n(Press ENTER to continue)\n")
            print("She walks Kemuri to the side a little and stops him when his weight is off his left hind leg.\nThen she grabs the leg and turns the hoof so it faces up. After cleaning this\nhoof she follows the same process to clean the right hind hoof.\n")
        else:
            print(dedent("""
            Dexterity Check above 20: You easily lift Kemuri's front hooves one by one and clean them.
                                      Then after a few tries you are able to clean his hind hooves as well.
            """))
            input("(Press ENTER to continue)")
            print("\nAki: Nice job!\n")
            self.stats.update_dexterity(1)
            self.stats.print_stats()
        input("(Press ENTER to continue)")

        print(dedent("""
               Aki: Now that that's done we're ready to put on the saddle.
                """))
        input("(Press ENTER to continue)")  
        print("\nAki throws a saddle blanket on Kemuri's back, followed by a saddle. After adjusting a bunch of\nbuckles she slips a halter on his head, tosses the reins over the saddle and hands you a lead rope.\n")
        input("(Press ENTER to continue)")
        print("\nAki: We're ready to go!\n")
        input("(Press ENTER to continue)")
        print("\nAki leads you to the practice field, and you follow leading Kemuri behind you.\n")
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: Although you want to trust in the instincts of your horse, you also need to
                    give clear instructions. Otherwise the horse will just take you wherever it
                    wants to go, which is probably the hay bale. So, before you even get on Kemuri,
                    why don't you walk him through the path your going to take? It will also give
                    you a chance to get comfortable leading him around.
                """))
        img = Image.open("res/horse_ride.png")
        img.show()
        print(dedent("""
               Aki: You're going to want to start here at the finish line. Then we go through 4 gates
                    before you get to gate F. After that you'll want to go through 3 more gates before 
                    arriving at gate J. Then you're almost done. You just have to go through the remainging gates 
                    and get back to the start line. Also you must never retrace or cross any path that you have
                    taken before.
                """))
        gate_order = None

        while gate_order != "gecbfilkjhda":
            gate_order, user_exit = self.input_exitable("Input the order that you go through the gates: ")
            if user_exit:
                return
            gate_order = gate_order.lower().translate({ord(c): '' for c in string.whitespace})
            if gate_order != "gecbfilkjhda":
                print("\nAki: I think we took a wrong turn. Let's go back to the start and try again.\n")

        print(dedent("""
               Aki: Great! Now you're ready to ride through the track. But it looks like Kemuri is starting
                    to get a bit unruly and its never good to get on a horse that isn't completly under your 
                    control. We can try riding the course tommorow. Kemuri should remember walking the course
                    with you.
                """))


        self.stats.update_dexterity(1)
        self.stats.print_stats()
        input("(Press ENTER to continue)")
        self.completed = True
