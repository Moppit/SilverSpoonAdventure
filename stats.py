# storing player stats and game status

class Stats:

    def __init__(self):

        # Bounds
        self.MIN = 1
        self.MAX = 20
        
        # Player stats -- default values
        self.dexterity = 7
        self.strength = 13
        self.social_intelligence = 16
        self.social_confidence = 12
        self.stamina = 20

        # Complete puzzles
        self.completed_puzzles = []

    def read_save_file(self, filename):
        # TODO: add to completed puzzles and player stats
        print("TODO")

    def new_puzzle_completed(self, puzzle_save_key):
        self.completed_puzzles.append(puzzle_save_key)

    def update_dexterity(self, delta):
        print()
        if(delta > 0):
            print("You feel your inner grace come out **Dexterity Level Up!**")
        if(delta < 0):
            print("You feel clumsy **Dexterity Level Down :(**")
        updated = self.dexterity + delta
        self.dexterity = max(self.MIN, min(self.MAX, updated))

    def update_strength(self, delta):
        print()
        if(delta > 0):
            print("This farm work is great for building muscles **Strength Level Up!**")
        if(delta < 0):
            print("You pulled a muscle from the strenuos work **Strength Level Down :(**")
        updated = self.strength + delta
        self.strength = max(self.MIN, min(self.MAX, updated))

    def update_social_intelligence(self, delta):
        print()
        if(delta > 0):
            print("You feel your understanding of other people's thoughts and emotions growing **Social Intelligence Level Up!**")
        if(delta < 0):
            print("Other people's thoughts and emotions start to feel a bit foggy to you **Social Intelligence Level Down :(**")
        updated = self.social_intelligence + delta
        self.social_intelligence = max(self.MIN, min(self.MAX, updated))

    def update_social_confidence(self, delta):
        print()
        if(delta > 0):
            print("The positive social interaction boosts your confidence **Social Confidence Level Up!**")
        if(delta < 0):
            print("Oops, you send something wrong and now you feel kind of nervous **Social Confidence Level Down :(**")
        updated = self.social_confidence + delta
        self.social_confidence = max(self.MIN, min(self.MAX, updated))

    def update_stamina(self, delta):
        print()
        if(delta > 0):
            print("Social interaction boosts your stamina, and you start to feel a skip in your step again **Stamina Increases**")
        if(delta < 0):
            print("This farm work is tiring! **Stamina Decreases**")

        updated = self.stamina + delta
        self.stamina = max(self.MIN, min(self.MAX, updated))