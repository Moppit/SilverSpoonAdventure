from puzzle import Puzzle
import sys
import time
from textwrap import dedent
sys.path.insert(0, './..')

class TokiwaTalk(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Talk to Tokiwa"
        self.save_key = "ETT"
        self.discussion_starters = [
            "How did you get so adept at handling chickens?",
            "How is school going?",
            "Heard any rumors around school lately?"]
        self.starters_finished = [False,False,False]

    def puzzle(self):
        while(True):
            print("\nWhat would you like to say?")
            for i in range(len(self.discussion_starters)):
                if not self.starters_finished[i]:
                    print(str(i) + ". " + self.discussion_starters[i])
            print(str(len(self.discussion_starters)) + ". Let's get back to work.")
            topic, user_quit = self.input_exitable(">> ")
            if user_quit:
                return
            if topic == "0":
                self.chicken_talk()
                self.starters_finished[0] = True
            elif topic == "1":
                self.school_talk()
                self.starters_finished[1] = True
            elif topic == "2":
                self.rumors_talk()
                self.starters_finished[2] = True
            elif topic == "3":
                print("Yeah, sure. We still have a lot to do today!")
                self.stats.update_social_confidence(2)
                self.stats.update_social_intelligence(1)
                self.stats.update_stamina(2)
                self.stats.print_stats()
                input("(Press ENTER to continue)\n")
                self.completed = True
                break
            else:
                print("\nTry Again\n")
        

        
    def chicken_talk(self):
        print(dedent("""
            Tokiwa: Chickens? Handling those little guys is second nature to me because
                    I've been raising them since I could walk. My family has a poultry farm,
                    and I'm ready to hold the reins if I ever need to!
        """))

    def school_talk(self):
        print(dedent("""
            Tokiwa: School is school. Hachiken gets me through the terrible, horrible, MATH
                    part of it, thankfully. And the rest is pretty cool, I guess.
        """))
    
    def rumors_talk(self):
        print(dedent("""
            Tokiwa: Aha!! You're a pretty sharp one for realizing that I am the KING
                    of rumors at this school, and on your first day no less! >:^)
                    Well, things have been kind of dry lately, but let me think... 
        """))
        input("(Press ENTER to continue)")

        print(dedent("""
            Tokiwa: Oh yeah, how could I forget! Y'know, Komaba, the star of the baseball team? He
                    just got the opportunity of a lifetime to play baseball in the US. Can you believe
                    it? I'm gonna miss that guy if he chooses to go, but hey y'know, the amount of
                    money he's gonna get from that offer is *insane*.
        """))
        input("(Press ENTER to continue)")

        print(dedent("""
            Tokiwa: Huh. That news wasn't really as juicy as I thought now that I've said it out loud.
                    Heh. Anyway, that's all I've got for now, ask me again when this place isn't so 
                    BORING, haha!
        """))
        input("(Press ENTER to continue)")
        
    