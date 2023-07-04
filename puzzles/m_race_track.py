from puzzle import Puzzle
import sys
from textwrap import dedent
from PIL import Image
import time
sys.path.insert(0, './..')

class RaceTrack(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Build a horse race track"
        self.save_key = "MRT"

    def puzzle(self):
        # TODO: add exit option
        print(dedent("""
              Aki: We're having a big race tomorrow and we need to build the track that 
                   the horses will be racing on. We were planning on setting up the same 
                   track we had last year... the only problem is no one remembers exactly 
                   how we had the track set up. 
              """))
        input("(Press ENTER to continue)")
        print(dedent("""
           Aki: So Nakajima Sensei ran a poll to see what people remembered and made a drawing 
                of what he found. 
           """))
        # Show drawing
        img = Image.open("res/race_track_puzzle.jpg")
        img.show()
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: Here's what Nakajima Sensei told me: 

                    "The drawing shows a number where each spectator was watching from along with 
                    an arrow showing which way they were facing. The number represents how many 
                    obstacles they saw while watching the race. Note that I did not count observers
                    as obstacles in the diagram"
                """))
        input("(Press ENTER to continue)")
        print(dedent("""
               Aki: Sounds pretty confusing to me, so I'll let you handle it. But I do rememeber 
                    some things that might be helpful. After we set up the race track, there weren't 
                    any empty spots left on the field. Every spot was either filled with an obstacle 
                    or a part of the race track. Also, the race track made a loop. Hopefully you can
                    piece all this information togther to figure out how the track was set up.
                """))
        input("(Press ENTER to continue)")
        num_obstacles = None
        while num_obstacles != 7:
            try:
                num_obstacles, user_quit = self.input_exitable(dedent("""
                    After filling in the diagram with a race track and obstacles
                    that match the observations, enter the number of obstacles used >> """))
                if user_quit:
                    return
                num_obstacles = float(num_obstacles)
                if not num_obstacles:
                    print("\nAki: I don't think thats a number, try again")
                elif num_obstacles < 7:
                    print("\nAki: I think I remember there being more obstacles")
                elif num_obstacles > 7:
                    print("\nAki: I don't remember there being so many obstacles")
            except:
                print("Aki: I don't think thats a number, try again")
           
        print(dedent(""" 
                    Aki peers over your shoulder as you are finishing up.
                    Aki: Ahhh... that looks familiar. I think you found the right setup. Thanks a lot!
                         Let's set up the race track.       
                """))
        self.stats.update_strength(2)
        self.stats.update_stamina(-3)
        self.stats.print_stats()
        input("(Press ENTER to continue)\n")
        self.completed = True
