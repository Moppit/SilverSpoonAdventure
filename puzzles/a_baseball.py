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
        self.huilins_team_blue = []
        self.opposing_team_red = []
        self.num_consecutive_correct = 0

    def puzzle(self):
        
        print(dedent("""
              Hachiken: Alright, lunch is ready! Let's call everyone over to eat!
              """))
        input("(Press ENTER to continue)")

        print("Lunch is over now, and the baseball game is about to commence!")
        # TODO: add the preface for why everyone runs over

        # Talk about how she hears the other team say, hey watch for the indicator
        print("As you walk to your position at second base, you hear the other team whispering to each other. 'Don't forget the indicator' they say")

        # Explain the symbols: note which letter means what

        # For each round, let her see the symbols, and let her guess steal vs. no steal
        # She must get 5 of them correct consecutively in order to tell Komaba
        while True:
            option = random.choice(["steals", "doesn't steal"])
            signs = self.generate_signs(option)
            print("You start intently as the coach signals to their team.")
            print("The coach makes the following signs:", signs)
            try:
                guess, user_quit = self.input_exitable("What do you guess? 'steals' or 'doesn't steal'? (or 'q' to exit): ")
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

            if self.num_consecutive_correct >= 5:
                print("You have gotten 5 correct in a row!")
                print("You quickly run up to the pitcher Komaba to tell him what you've discerned.")
                print("Komaba: Oh hey! Did you figure out which action is the indicator?")
                guessIndicator, user_quit = self.input_exitable("(enter H, N, S, C, E, A, or 'q' to exit): ")
                if user_quit:
                    return
                if guessIndicator == self.indicator:
                    print("Komaba: Gotcha! Intuitively, that seems right. Do you know which action indicates a steal?")
                    guessSteal, user_quit = self.input_exitable("(enter H, N, S, C, E, A, or 'q' to exit): ")
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
