from puzzle import Puzzle
import sys
import time
from textwrap import dedent
from PIL import Image
sys.path.insert(0, './..')

class AkiTalk(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Talk to Aki"
        self.save_key = "MAT"
        self.discussion_starters = [
            "You really seem to care about horses. Why do you like them so much?",
            "The weather is really nice today isn't it?",
            "How are Hachiken kun and your other friends doing?"]
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
                self.horse_talk()
                self.starters_finished[0] = True
            elif topic == "1":
                self.weather_talk()
                self.starters_finished[1] = True
            elif topic == "2":
                self.friends_talk()
                self.starters_finished[2] = True
            elif topic == "3":
                print("Yeah, sure. We still have a lot to do today!")
                self.stats.update_social_confidence(2)
                self.stats.update_social_intelligence(1)
                self.stats.update_stamina(1)
                self.stats.print_stats()
                input("(Press ENTER to continue)\n")
                self.completed = True
                break
            else:
                print("\nTry Again\n")
        

        
    def horse_talk(self):
        print(dedent("""
            Aki: I feel like horses are almost like people in so many ways and I respect them 
                 for that. See how the other horses help Maron? It's just like how humans might
                 say... take care of a sick grandmother.
        """))
        stat_check = None
        while True:
            print("Roll a d20 for Social Intelligence to see how well you can read her as she is talking\nYou can find one at https://flipsimu.com/dice-roller/roll-d20/")
            roll, user_quit = self.input_exitable("Enter result >> ")
            if user_quit:
                return
            try:
                stat_check = int(roll.strip()) + self.stats.social_intelligence
                break
            except:
                print("Enter an integer")
        if int(roll) == 1:
            print("\nNatural 1: You notice she likes horses a lot.\n")
            input("(Press ENTER to continue)")
            print("\nHuilin: Yeah, horses are pretty cool, aren't they?")
        elif stat_check < 25:
            print("\nYou notice that there's something else on her mind.")
            response, user_quit = self.input_exitable("Do you ask her what's on her mind? >> ")
            if user_quit:
                return
            if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
                print("\nRoll a d20 for Social Confidence to see if you are confident enough to question her further.")
                roll, user_quit = self.input_exitable("Enter result >> ")
                if user_quit:
                    return
                stat_check = int(roll) + self.stats.social_confidence
                if stat_check < 15:
                    print("\nSocial Confidence Check less than 15: You do not feel confident enough to ask.\n")
                    input("(Press ENTER to continue)")
                    print("\nHuilin: Yeah, horses are pretty cool, aren't they?")
                else:
                    print("\nSocial Confidence Check of 15 or more: You feel confident enough to probe further.\n")
                    input("(Press ENTER to continue)")  
                    print("\nHuilin: Is there something else on your mind?\n")
                    input("(Press ENTER to continue)\n")
                    print("Aki: No... well yes I guess. I'm just thinking about a friend.\n")
                    input("(Press ENTER to continue)\n")

                    response, user_quit = self.input_exitable("Do you ask her which friend? >> ")
                    if user_quit:
                        return
                    if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
                        stat_check = None
                        while True:
                            print("Roll a d20 for Social Confidence to see if you are confident enough to question her further.")
                            roll, user_quit = self.input_exitable("Enter result >> ")
                            if user_quit:
                                return
                            try:
                                stat_check = int(roll.strip()) + self.stats.social_intelligence
                                break
                            except:
                                print("Enter an integer")
                        
                        if stat_check < 25:
                            print("\nSocial Confidence Check less than 25: You feel it would be impolite to question further.\n")
                            input("(Press ENTER to continue)")
                            print("\nHuilin: I see.")
                        else:
                            print("\nSocial Confidence Check of at least 25: You feel confident enough to keep probing\n")
                            input("(Press ENTER to continue)")
                            print("\nHuilin: Which friend? Are they alright?\n")
                            input("(Press ENTER to continue)\n")
                            print("Aki hesitates\n")
                            input("(Press ENTER to continue)\n")
                            print("Aki: I don't want to bother you with problems that don't involve you...\n")
                            input("(Press ENTER to continue)")
                            print(dedent("""
                                Aki: Your just like Hachiken, wanting to help everyone out even though it's
                                     only your first day! It's Komaba. Although he also seems so stoic, 
                                     he's actually having a bit of a tough time right now.
                            """))
                            input("(Press ENTER to continue)")
                            print(dedent("""
                                Huilin: People like that are often the people who need the most help since
                                        they don't ask for help even when they need it.
                            """))
                    else:
                        print("\nHuilin: I see.")
        elif stat_check < 30:
            print(dedent("""
                Social Intelligence Check of 25 or more: She is thinking of a particular 
                                                         human who has a sick grandmother.
            """))
            input("(Press ENTER to continue)\n")
            response, user_quit = self.input_exitable("Do you ask her who she is thinking of? >> ")
            if user_quit:
                return
            if response.lower().strip() != "no" and response.lower().strip() != "n":
                stat_check = None
                while True:
                    print("\nRoll a d20 for Social Confidence to see if you are confident enough to question her further.")
                    roll, user_quit = self.input_exitable("Enter result >> ")
                    if user_quit:
                        return
                    try:
                        stat_check = int(roll.strip()) + self.stats.social_intelligence
                        break
                    except:
                        print("Enter an integer")
                
                if stat_check < 20:
                    print(dedent("""
                        "Social Confidence Check less than 20: You do not feel confident enough to call out
                                                               the connection you made"
                    """))
                    input("(Press ENTER to continue)")
                    print("\nHuilin: Yeah, horses are pretty cool, aren't they?")
                else:
                    print(dedent("""
                        Social Confidence Check of at least 20: You feel confident enough to talk about
                                                                what you are thinking.
                            """))
                    input("(Press ENTER to continue)")
                    print("\nHuilin: So... are you thinking of anyone in particular with a sick grandmother?")
                    input("(Press ENTER to continue)\n")
                    print("Aki: It's one of my good friends. He really cares for her a lot.")
            else:
                print("\nHuilin: Yeah, horses are pretty cool, aren't they?")
        else:
            print(dedent("""
                Social Intelligence Check greater than 30: She is thinking of a friend who wants to take care of a sick
                                                           grandmother, and she also seems a bit sad for some reason.
                        """))
            input("(Press ENTER to continue)\n")
            response, user_quit = self.input_exitable("Do you ask her who she is thinking of and why she's a bit sad? >> ")
            if user_quit:
                return
            if response.lower().strip() != "no" and response.lower().strip() != "n":
                stat_check = None
                while True:
                    print("\nRoll a d20 for Social Confidence to see if you are confident enough to question her further.")
                    roll, user_quit = self.input_exitable("Enter result >> ")
                    if user_quit:
                        return
                    try:
                        stat_check = int(roll.strip()) + self.stats.social_intelligence
                        break
                    except:
                        print("Enter an integer")
                if stat_check < 20:
                    print("\nSocial Confidence Check less than 20: You do not feel confident enough to call out the connection you made")
                    input("\n(Press ENTER to continue)")
                    print("\nHuilin: Yeah, horses are pretty cool, aren't they?")
                else:
                    print("\nSocial Confidence Check of at least 20: You feel confident enough to talk about what you are thinking.")
                    input("\n(Press ENTER to continue)")
                    print(dedent("""
                        Huilin: So... does one of your friends have a sick grandmother? 
                                And you seem a little sad, is everything okay?
                                """))
                    input("(Press ENTER to continue)")
                    print(dedent("""
                        Aki: Yeah, it's Komaba kun. He's usually seems unaffected by everything life throws his way, but 
                             I know it's been really tough on him... I wish I could help him more.
                    """))

            
        if user_quit:
            return
    def weather_talk(self):
        print(dedent("""
            Aki: Yeah it is. A nice day for horseback riding, or a game of baseball.
        """))
    
    def friends_talk(self):
        print(dedent("""
            Aki: Hachiken kun is doing great! He's finally cut back a little on his workload and he's
                 enjoying the farm school life. Everyone's also really excited that the baseball team
                 managed to win the Hokkaido regional tornament. I guess everyone except Komaba, he's
                 been uncharacteristically serious lately.
        """))
        
    