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
        updated = self.dexterity + delta
        self.dexterity = max(self.MIN, min(self.MAX, updated))

    def update_strength(self, delta):
        updated = self.strength + delta
        self.strength = max(self.MIN, min(self.MAX, updated))

    def update_social_intelligence(self, delta):
        updated = self.social_intelligence + delta
        self.social_intelligence = max(self.MIN, min(self.MAX, updated))

    def update_social_confidence(self, delta):
        updated = self.social_confidence + delta
        self.social_confidence = max(self.MIN, min(self.MAX, updated))

    def update_stamina(self, delta):
        updated = self.stamina + delta
        self.stamina = max(self.MIN, min(self.MAX, updated))