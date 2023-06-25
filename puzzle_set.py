# group of puzzles, plus the dialogue for that group

class PuzzleSet:

    def __init__(self, stats, puzzles, set_complete=False):
        self.stats = stats
        self.puzzles = puzzles
        self.set_complete = set_complete

    def get_input(self, lower, upper):
        # read 
        # validate
        print("TODO: get input from user!")
        return 0 # return what was entered once we get something valid

    def run(self):
        
        while(True):
            # Display the puzzle choices & exit option
            print("What do you want to do?")
            num_puzzles = len(self.puzzles)
            for i in range(num_puzzles):
                print(i, "-", self.puzzles[i].description)
            print(num_puzzles, "-", "Exit")

            # If she choses exit
            entered = self.get_input(0, num_puzzles)
            if(entered == num_puzzles):
                return self.stats

            # Run the puzzle that is selected if not already completed
            # - if she exits in middle, don't save that partial instance
            self.puzzles[entered].stats = self.stats
            new_stats = self.puzzles[entered].run()

            # Save finished puzzle in stats object
            if self.puzzles[entered].completed:
                self.stats = new_stats

            # If all puzzles completed, exit
            for puzzle in self.puzzles:
                if not puzzle.completed:
                    continue
            
            # If all puzzles are complete, exit loop
            self.set_complete = True
            break
        
        # Return stats
        return self.stats