from puzzle import Puzzle
import sys
import time
from textwrap import dedent
sys.path.insert(0, './..')

class KomabaTalk(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Talk to Komaba"
        self.save_key = "NKT"
        self.discussion_starters = [
            "How is [Insert friend or family member here]?",
            "Can you tell me more about the baseball opportunity?",
            "Let me teach you how to break baseball signs."]
        self.starters_finished = [False,False,False]

    def puzzle(self):
        while(True):
            print("\nWhat would you like to say?")
            for i in range(len(self.discussion_starters)):
                if not self.starters_finished[i]:
                    print(str(i) + ". " + self.discussion_starters[i])
            print(str(len(self.discussion_starters)) + ". *Yawn* It's pretty late, I've got to get to bed.")
            topic, user_quit = self.input_exitable(">> ")
            if user_quit:
                return
            if topic == "0":
                self.person_talk()
            elif topic == "1":
                self.baseball_talk()
                self.starters_finished[1] = True
            elif topic == "2":
                self.baseball_sign_talk()
                self.starters_finished[2] = True
            elif topic == "3":
                print(dedent("""
                Komaba: Yeah, I've got to get up early tommorow to practice. Thanks for talking to me.
                        I think talking to you has helped me make my decsion about the offer.
                """))
                self.stats.update_social_intelligence(2)
                self.stats.update_stamina(2)
                self.stats.update_social_confidence(10)
                self.stats.print_stats()
                input("(Press ENTER to continue)")
                self.completed = True
                break
            else:
                print("\nTry Again\n")
        


    def person_talk(self):
        person, user_quit = self.input_exitable("Who would you like to ask about >> ")
        if user_quit:
            return
        if person.lower() == "aki" or person.lower() == "aki san":
            print("\nHuilin: How is Aki san?\n")
            input("(Press ENTER to continue)")
            print(dedent("""
            Komaba: Aki is good. She's still riding horses and it's great that she can keep doing
                    what she is passionate about. She really has been like a sister to me... having
                    grown up as neihbors. I really do hope for the best for her.
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
            if stat_check < 20:
                print("\nSocial Intelligence Check of 19 or less: You notice he's feeling nostalgic.\n")
                self.aki_talk()
            elif stat_check < 25:
                print("\nYou notice that he's feeling really nostalgic about those times, almost like those times are over.\n")
                self.aki_talk()
            else:
                print(dedent("""
                    Social Intelligence Check of at least 20: You notice that he's feeling really nostalgic about those times, almost like
                                                              those times are over. It's uncommon to see him be so expressive with his
                                                              emotions.
                """))
                self.aki_talk()
        elif person.lower() == "tokiwa" or person.lower() == "tokiwa kun":
            print("\nHuilin: How is Tokiwa kun?\n")
            input("(Press ENTER to continue)")
            print(dedent("""
            Komaba: Tokiwa is his usually goofy self. Did he try playing egg mancala with you too? Sometimes I wonder about him.
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
            if stat_check < 30:
                print("\nSocial Intelligence Check of 29 or less: You don't detect much other than the teasing that comes from a comfortable friendship.\n")
            else:
                print(dedent("""
                    Social Intelligence Check of at least 20: Behind his nonchalant words you notice that he actually does care for Tokiwa and
                                                              you're sure he'll actually miss Tokiwa a lot.
                """))
            input("(Press ENTER to continue)")
            print("\nHuilin: Yeah we played egg mancala... It was actually pretty fun!\n")
        elif person.lower() == "hachiken" or person.lower() == "hachiken kun":
            print("\nHuilin: How is Hachiken kun?\n")
            input("(Press ENTER to continue)")
            print(dedent("""
            Komaba: Hachiken is good. He still helps everyone and he seems to really be developing his sense of 
                    purpose. I'm really going to miss his cooking... If I accept the offer.
            """))
            stat_check = None
            while True:
                print("Roll a d20 for Social Intelligence to see how well you can read him as he is talking.\nYou can find one at https://flipsimu.com/dice-roller/roll-d20/")
                roll, user_quit = self.input_exitable("Enter result >> ")
                if user_quit:
                    return
                try:
                    stat_check = int(roll.strip()) + self.stats.social_intelligence
                    break
                except:
                    print("Enter an integer")
            if stat_check < 30:
                print(dedent("""
                Social Intelligence Check of 29 or less: You haven't noticed till now since everyone here loves food,
                                                                         but he is almost as passionate about food as he is about
                                                                         baseball.
                                                                         """))
            else:
                print(dedent("""
                    Social Intelligence Check of at least 30: You notice that, while he said Hachiken's cooking, he really meant
                                                              Hachiken. He does still love the food though. Everyone here's a
                                                              little obsessed with food.
                """))
            input("(Press ENTER to continue)")
            print("\nHuilin: Hachiken is pretty particular about his cooking, but the end result is definately worth it!\n")
        elif person.lower() == "dad" or person.lower() == "grandfather" or person.lower() == "grandpa":
            print("\nHuilin: How is your " + person.lower() + " doing?\n")
            input("(Press ENTER to continue)")
            print(dedent("""
            Komaba: My {0} is doing good. I will miss him if I leave though.
            """.format(person.lower())))
        elif person.lower() == "mom" or person.lower() == "sister":
            print("\nHuilin: How is your " + person.lower() + " doing?\n")
            input("(Press ENTER to continue)")
            print(dedent("""
            Komaba: My {0} is doing good. I will miss her if I leave though.
            """.format(person.lower())))
        elif person.lower() == "sisters" or person.lower() == "twins":
            print("\nHuilin: How are your sisters doing?\n")
            input("(Press ENTER to continue)")
            print(dedent("""
            Komaba: My sisters are doing good. They will miss me a lot if I leave though.
            """.format(person.lower())))
        elif person.lower() == "grandmother" or person.lower() == "grandma":
            print("\nKomaba: My grandmother...\n")
            input("(Press ENTER to continue)")
            print("\nKomaba narrows his eyes.\n")
            input("(Press ENTER to continue)")
            print(dedent("""
                Komaba: So you know do you? Well, yeah she's sick.
                """))
            input("(Press ENTER to continue)")
            response,user_quit = self.input_exitable("\nDo you probe him further? ")
            if user_quit:
                return
            if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
                response_asked = [False,False,False]
                while(True):
                    print("\nWhat do you ask about?") # How old is she, How serious is it, Will you miss her
                    if response_asked[0] == False:
                        print("1. How serious is it?")
                    if response_asked[1] == False:
                        print("2. How old is she?")
                    if response_asked[2] == False:
                        print("3. Will you miss her?")
                    print("4. Nevermind")
                    
                    response, user_quit = self.input_exitable(">> ")
                    if user_quit:
                        return
                    elif response == "4":
                        print(dedent("""
                        Huilin: I hope she gets better soon and lives to see you become a baseball super star!
                                I'm sure your family will be able to take care of her just fine without you.
                        """))
                        break
                    elif response == "1" and response_asked[0] == False:
                        print("\nHuilin: How serious is her illness?\n")
                        input("(Press ENTER to continue)")
                        print("\nKomaba: It's pretty serious. The medical bills are starting to pile up.\n")
                        response_asked[0] = True
                    elif response == "2" and response_asked[1] == False:
                        print("\nHuilin: How old is she?\n")
                        input("(Press ENTER to continue)")
                        print("\nKomaba: She's 85, so she's getting pretty old.\n")
                        response_asked[1] = True
                    elif response == "3" and response_asked[2] == False:
                        print("\nHuilin: Will you miss her?\n")
                        input("(Press ENTER to continue)")
                        print("\nKomaba: She needs someone to take care of her. It will be tough on the others if I won't be around to help.\n")
                        input("(Press ENTER to continue)")
                        stat_check = None
                        while True:
                            print("Roll a d20 for Social Intelligence to see how well you can read him as he is talking.\nYou can find one at https://flipsimu.com/dice-roller/roll-d20/")
                            roll, user_quit = self.input_exitable("Enter result >> ")
                            if user_quit:
                                return
                            try:
                                stat_check = int(roll.strip()) + self.stats.social_intelligence
                                break
                            except:
                                print("Enter an integer")
                        if stat_check < 25:
                            print("\nSocial Intelligence Check of less than 25: He really seems to take his duty of taking care of her seriously.\n")
                        else:
                            print(dedent("""
                                Social Intelligence Check of at least 25: He will actually miss taking care of her a lot. It's going to be really tough 
                                                                          for him to leave his sick grandmother and go to a different country. It looks
                                                                          like this might be the main reason he's hesitant to accept the offer.
                                """))
                        response_asked[2] = True
                    else:
                        print("\nInvalid response\n")
                print("")
        else:
            print("\nKomaba: Sorry, who do you mean?")

    def aki_talk(self):
        response, user_quit = self.input_exitable("Do you probe further? ")
        if user_quit:
            return
        if response.lower().strip() == 'yes' or response.lower().strip() == 'y':
            stat_check = None
            while True:
                print("\nRoll a d20 for Social Confidence to see if you are confident enough to question her further.")
                roll, user_quit = self.input_exitable("Enter result >> ")
                if user_quit:
                    return
                try:
                    stat_check = int(roll) + self.stats.social_confidence
                    break
                except:
                    print("Enter an integer")

            if int(roll) == 1:
                print("\nNatural 1: You do not feel confident enough to ask.\n")
                input("(Press ENTER to continue)")
                print("\nHuilin: Yeah, Aki's pretty cool!")
            else:
                print("\nYou feel confident enough to probe further.\n")
                input("(Press ENTER to continue)")  
                print("\nHuilin: You're going to miss her aren't you?\n")
                input("(Press ENTER to continue)")
                print("\nKomaba: ...\n")
                input("(Press ENTER to continue)")
                print("\nKomaba: Yeah I will. I guess its one of the reasons I haven't accepted the baseball offer yet.\n")
        else:
            print("Huilin: Yeah, Aki's pretty cool!")

    def baseball_talk(self):
        print(dedent("""
            Huilin: Can you tell me more about the baseball opportunity? It sounds really exciting!
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
            Komaba: A talent scout from the Colorado Rockies came to Japan to visit his friend who
                    coaches the team at the University of Tokyo. It happened to be at the same time 
                    that I was doing a summer camp there. He watched me play a game and he was 
                    impressed by what he saw. And now here I am with an offer to play for the
                    Colorado Rockies!
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
            Huilin: Wow! That's quite the good luck you had! It's amazing to get an opportunity
                    to follow your dream's... And I actually live in Colorado, it's a great 
                    place to live!
        """))
        input("(Press ENTER to continue)")
        response, user_quit = self.input_exitable(dedent("""
            Do you ask him about the money he will earn and how he will use it? """))
        if user_quit:
            return
        if response == 'y' or response == 'yes':
            stat_check = None
            while True:
                print("\nRoll a d20 for Social Confidence to see if you are confident enough to question him about money.")
                roll, user_quit = self.input_exitable("Enter result >> ")
                if user_quit:
                    return
                try:
                    stat_check = int(roll) + self.stats.social_confidence
                    break
                except:
                    print("Enter an integer")

            if stat_check < 20:
                print(dedent("""
                    Social Confidence Check less than 20: You feel it would not be appropriate to ask him about money.
                """))
                input("(Press ENTER to continue)")
            else:
                print(dedent("""
                    Social Confidence Check of at least 20: You confident enough to ask him about money.
                """))
                input("(Press ENTER to continue)")
                print("\nHuilin: So... You'll be making a lot of money right? That will be helpful for your family's finacial situation, won't it?\n")
                input("(Press ENTER to continue)")
                print(dedent("""
                    Komaba: Yeah, it should pay my grandmother's medical bills in the short term, and in the long run
                            I should have enough to pay off the family debt and eventually buy back the farm.
                """))
                input("(Press ENTER to continue)")
                print("\nHuilin: I see... yes that would be nice. But of course it's never easy to leave your home behind.\n")
                self.starters_finished[1] = True
                input("(Press ENTER to continue)")
    
    def baseball_sign_talk(self):
        print(dedent("""
            Huilin: Alright, let me tell you how I broke the baseball signs...
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
            You tell Komaba about the wonders of codes and ciphers and linguistics.
        """))
        input("(Press ENTER to continue)")
        print("\n15 Minutes Later\n")
        input("(Press ENTER to continue)")
        print(dedent("""
            ... and with that I had the final key to deciphering the syntax of the baseball sign language.
        """))
        input("(Press ENTER to continue)")
        print(dedent("""
            Komaba: Impressive! It's too much math and language for me. I'll just leave this kind of stuff to you and Hachiken.
        """))
        input("(Press ENTER to continue)")
        
    