from puzzle import Puzzle
import sys
from textwrap import dedent
from PIL import Image
import time
import random
import string
sys.path.insert(0, './..')

class Baseball(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Let's play ball!"
        self.save_key = "APB"
        self.movements = {
            "H": "Hat",
            "N": "Nose",
            "S": "Shoulder",
            "E": "Ear",
            "C": "Chin",
            "A": "Arm"
        }
        self.indicator = "C"
        self.steal = "E"
        self.huilins_team_blue = ["Komaba (captain)", "Huilin", "Tokiwa", "Aki", "Beppu"]
        self.opposing_team_red = ["Shin-ichiro Inada (captain)", "Hachiken", "Aikawa", "Tamako Inada", "Yoshino"]
        self.num_consecutive_correct = 0

    def puzzle(self):
        
        print(dedent("""
              Hachiken: Alright, lunch is ready! Let's call everyone over to eat!
              """))
        input("(Press ENTER to continue)")

        print("Lunch is over now, and the baseball game is about to commence!\n")
        print("Hachiken: Okay, I've randomly generated teams!")
        print("          Blue team:", ' ,'.join(self.huilins_team_blue))
        print("          Red team:", ' ,'.join(self.opposing_team_red))
        input("(Press ENTER to continue)")

        # Talk about how she hears the other team say, hey watch for the indicator
        print(dedent("""\n
            As you walk to your position at second base, you hear the other team's captain, Shin-ichiro Inada,
            whispering to his team.

            Shin-ichiro Inada: Don't forget the indicator!
        """))
        input("(Press ENTER to continue)")

        # Explain the symbols: note which letter means what
        print(dedent("""
            You realize, the other team is going to use baseball signs! You remember from reading 
            about baseball signs a while ago, that a baseball sign is usually an indicator
            (i.e. a movement to signal when important information is coming), followed by a
            cue to act. The rest of the movements are supposed to distract from the intended 
            message.
        """))
        input("(Press ENTER to continue)")

        print(dedent("""
            If you can interpret the signs, that would be a huge boost to your team. You run up 
            to Komaba, your team's captain, to tell him your plan.

            Huilin: Komaba! I think the other team will be using baseball signs. I'm going to try
                    to crack it.
        """))

        print(dedent("""
            Komaba: Oh really? That's a cool idea, I haven't tried that before. Cracking an
                    opposing team's baseball signs is supposed to be pretty hard. If you can 
                    do it, please let me know what you find.
        """))
        input("(Press ENTER to continue)")

        print("\n\nAnd the game begins!\n\n")
        input("(Press ENTER to continue)")

        print("You notice the following gestures being used by Inada:")
        for item in self.movements:
            print(item, ":", self.movements[item])

        # For each round, let her see the symbols, and let her guess steal vs. no steal
        while True:
            option = random.choice(["steals", "doesn't steal"])
            signs = self.generate_signs(option)
            print("You stare intently as the coach signals to their team.")
            print("The coach makes the following signs:", signs)
            try:
                guess, user_quit = self.input_exitable("What do you guess? 'steals' or 'doesn't steal'? (or 'q' to exit the game): ")
                if user_quit:
                    return

                print("You watch the result -- the team", option)
                if guess == option:
                    self.num_consecutive_correct += 1
                    print("You were correct! That's", self.num_consecutive_correct, "correct guesses in a row.")
                else:
                    
                    self.num_consecutive_correct = 0
                    print("Your guess wasn't right")
            except:
                pass

            if self.num_consecutive_correct >= 3:
                print()
                print("You have gotten 3 correct in a row!")
                print("You quickly run up to the pitcher Komaba to tell him what you've discerned.")
                print("Komaba: Oh hey! Did you figure out which action is the indicator?")
                guessIndicator, user_quit = self.input_exitable("(enter H, N, S, C, E, A, or 'q' to exit the game): ")
                if user_quit:
                    return
                if guessIndicator == self.indicator:
                    print("Komaba: Gotcha! Intuitively, that seems right. Do you know which action indicates a steal?")
                    guessSteal, user_quit = self.input_exitable("(enter H, N, S, C, E, A, or 'q' to exit the game): ")
                    if user_quit:
                        return
                    if guessSteal == self.steal:
                        print("Komaba: Roger that! Let's give this a go!")
                        break
                    else:
                        self.num_consecutive_correct = 0
                        print("Komaba: Hmm, I'm not sure why, but that doesn't seem right. Maybe keep observing?")
                else:
                    self.num_consecutive_correct = 0
                    print("Komaba: Hmm, I'm not sure why, but that doesn't seem right. Maybe keep observing?")
            print()

        print("\nThe game continues, and Komaba anticipates their every move.")
        print("\nGame Announcer: And the winning team is: the Blue Team!")
        print("\nThe audience roars!! That's the game!")
        input("(Press ENTER to continue)")

        self.stats.update_strength(2)
        self.stats.update_stamina(-2)
        self.stats.print_stats()
        input("(Press ENTER to continue)")
        self.completed = True

    def generate_signs(self, is_steal):
        # If it's a steal, use the given key
        # Sequence is 10 characters long
        chars = []
        num_chars = 10
        if is_steal == "steals":
            chars.append(self.indicator + self.steal)
            num_chars -= 2
        else:
            chars.append(self.indicator)
            num_chars -= 1
        
        # Add the rest of the letters
        choices = ["H", "N", "S", "E", "A"]
        for i in range(num_chars):
            chars.append(random.choice(choices))

        # Randomize
        randomized = None
        while not randomized:
            random.shuffle(chars)
            for i in range(len(chars)-1):
                if chars[i] != self.indicator and chars[i+1] != self.steal:
                    randomized = True

        return "".join(chars)
