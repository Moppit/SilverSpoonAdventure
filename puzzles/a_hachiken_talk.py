from puzzle import Puzzle
import sys
import time
from textwrap import dedent
from PIL import Image
sys.path.insert(0, './..')

class HachikenTalk(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Talk to Hachiken"
        self.save_key = "AHT"
        self.discussion_starters = [
            "You really seem to care about pigs. Why do you like them so much?",
            "Everyone seems really excited for this pizza, huh?",
            "How are Komaba kun and your other friends doing?"]
        self.starters_finished = [False,False,False]

    def puzzle(self):

        # Show the situation where Komaba comes to grab pizza
        print(dedent("""
            You turn to speak to Hachiken kun, but before you get a word in...
        """))
        print(dedent("""
         Komaba: Hey! Hachiken!
        """))
        print(dedent("""
         Hachiken looks up to see Komaba running toward you both.
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
         Hachiken: Classic Komaba, I knew you'd be here soon! I bet you're here 
                   to get ahead on preparing for the game, right? Trying to pack in the 
                   calories and allow "adequate digesting time"?
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
         Komaba: Woooow Hachiken, I can even hear the air quotes in your voice, it's
                 a real thing you know!
                 ...
                 So yes heh, that's exactly what I'm here for. Hachiken, you really know 
                 me too well.
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
         Hachiken: Dude, it doesn't take a genius to see how diligent you are about baseball.
                   The pizza isn't ready yet unfortunately, but let me sneak you a banana. Come
                   back in a bit, and it should be ready!
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
         Komaba: Thanks Hachiken! Alright, I'll be back.
        """))
        print(dedent("""
         Komaba runs off toward the baseball field, probably to practice some more.
        """))
        input("(Press ENTER to continue)")

        # Start talking
        while(True):
            print("\nWhat would you like to say? (or type 'q' to exit)")
            for i in range(len(self.discussion_starters)):
                if not self.starters_finished[i]:
                    print(str(i) + ". " + self.discussion_starters[i])
            print(str(len(self.discussion_starters)) + ". Let's get back to work.")
            topic, user_quit = self.input_exitable(">> ")
            if user_quit:
                return
            if topic == "0":
                self.pig_talk()
                self.starters_finished[0] = True
            elif topic == "1":
                self.pizza_talk()
                self.starters_finished[1] = True
            elif topic == "2":
                self.friends_talk()
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
        

        
    def pig_talk(self):
        print(dedent("""
            Hachiken: Oh yeah, how could you not? Pigs are so sweet and smart. It took me a while 
                      to get over the idea of eating them, they're that cute. Butadon was my 
                      favorite. But alas, I can't give up bacon.
        """))
    
    def pizza_talk(self):
        print(dedent("""
            Hachiken: For sure, we only recently found the pizza oven, so it
                      makes sense that everyone is still crazy for it. Did you
                      know that everyone helped gather the ingredients for this
                      pizza? I love this school, everyone here is just too kind.
        """))
    
    def friends_talk(self):
        print(dedent("""
       Hachiken: Oh, my friends? Everyone is doing great! Well, Komaba is a bit serious
                 these days, but... y'know, he's still knocking it out of the park, literally
                 haha.
        """))
        stat_check = None
        while True:
            print("Roll a d20 for Social Intelligence to see how well you can read him as he is talking\nYou can find one at https://flipsimu.com/dice-roller/roll-d20/")
            roll, user_quit = self.input_exitable("Enter result >> ")
            if user_quit:
                return
            try:
                stat_check = int(roll.strip()) + self.stats.social_intelligence
                break
            except:
                print("Enter an integer")
        if int(roll) == 1:
            print("Natural 1: You notice he has a lot of goodwill for his best friend, Komaba kun.")
            print("\nHuilin: Yeah, I can't wait to see Komaba kun play at the game after lunch!")
        elif stat_check < 25:
            print("You notice that there's something else on his mind.")
            response, user_quit = self.input_exitable("Do you ask him what's on his mind? >> ")
            if user_quit:
                return
            if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
                print("Roll a d20 for Social Confidence to see if you are confident enough to question him further.")
                roll, user_quit = self.input_exitable("Enter result >> ")
                if user_quit:
                    return
                stat_check = int(roll) + self.stats.social_confidence
                if stat_check < 15:
                    print("Social Confidence Check less than 15: You do not feel confident enough to ask.")
                    print("\nHuilin: Yeah, I can't wait to see Komaba kun play at the game after lunch!")
                else:
                    print("Social Confidence Check of 15 or more: You feel confident enough to probe further.")
                    print("\nHuilin: Is there something else on your mind?")
                    input("(Press ENTER to continue)\n")
                    print("Hachiken: Ah, not much... I was just thinking about how private he is sometimes.")

                    response, user_quit = self.input_exitable("Do you ask him what he means by that? >> ")
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
                            print("Social Confidence Check less than 25: You feel it would be impolite to question further.")
                            print("\nHuilin: I see.")
                        else:
                            print("Social Confidence Check of at least 25: You feel confident enough to keep probing")
                            print("\nHuilin: What do you mean by that?")
                            input("(Press ENTER to continue)\n")
                            print(dedent("""
                           Hachiken: Ah, I just mean he always tries to do everything by himself, even if it's hard. It's 
                                     one of the things I admire a lot about him. But I wish he'd accept help sometimes.
                                     What else are friends for?
                            """))
                            print(dedent("""
                                Huilin: I see, that's a tough situation.
                            """))
                    else:
                        print("\nHuilin: I see.")
        elif stat_check < 30:
            print(dedent("""
                Social Intelligence Check of 25 or more: He seems concerned, and maybe a little frustrated.
            """))
            response, user_quit = self.input_exitable("Do you ask him if he's concerned? >> ")
            if user_quit:
                return
            if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
                stat_check = None
                while True:
                    print("Roll a d20 for Social Confidence to see if you are confident enough to question him further.")
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
                        "Social Confidence Check less than 20: You do not feel confident enough to ask."
                    """))
                    print("\nHuilin: Yeah, I can't wait to see Komaba kun play at the game after lunch!")
                else:
                    print(dedent("""
                        Social Confidence Check of at least 20: You feel confident enough to ask."""))
                    print("\nHuilin: Is everything okay? You seem like you might be a bit concerned.")
                    input("(Press ENTER to continue)\n")
                    print("Hachiken: Oh, I mean I'm okay -- I just worry about Komaba sometimes. I wish he'd let me help him.")
            else:
                print("\nHuilin: Yeah, I can't wait to see Komaba kun play at the game after lunch!")
        else:
            print(dedent("""
                Social Intelligence Check greater than 30: He seems a little worried about Komaba kun, and maybe a little frustrated.
                        """))
            response, user_quit = self.input_exitable("Do you ask him why he's worried about Komaba kun? >> ")
            if user_quit:
                return
            if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
                stat_check = None
                while True:
                    print("Roll a d20 for Social Confidence to see if you are confident enough to question him further.")
                    roll, user_quit = self.input_exitable("Enter result >> ")
                    if user_quit:
                        return
                    try:
                        stat_check = int(roll.strip()) + self.stats.social_intelligence
                        break
                    except:
                        print("Enter an integer")
                if stat_check < 20:
                    print("Social Confidence Check less than 20: You do not feel confident enough to ask him further.")
                    print("\nHuilin: Yeah, I can't wait to see Komaba kun play at the game after lunch!")
                else:
                    print("Social Confidence Check of at least 20: You feel confident enough to talk about what you are thinking.")
                    print(dedent("""
                        Huilin: So... is Komaba kun okay? You seem a little worried about him.
                                """))
                    print(dedent("""
                   Hachiken: Yeah, I probably worry about him too much, but that's the hazard of being best friends, right? Haha. 
                             I know he's strong and will be okay no matter what, but he has a lot of weight on his shoulders. 
                             I just wish I could help him more, maybe help carry some of the burdens. He would never allow
                             that though.
                    """))

            
        if user_quit:
            return
        
    