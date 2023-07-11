from puzzle import Puzzle
import sys
import time
import random
from textwrap import dedent
sys.path.insert(0, './..')

class ChickenEggs(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Collect the chicken eggs"
        self.save_key = "ECE"
        self.board = [ [4 for i in range(6)] for j in range(2) ]
        self.tokiwas_bucket = 0
        self.huilins_bucket = 0
        self.huilins_turn = True
        self.huilin_won = False

    def puzzle(self):
        print(dedent("""
           Tokiwa: Woohoo, chickens! Here's the chicken coop. 
                   ...
                   Yoooooo do you wanna do something fun? Let's play Mancala with
                   these chicken eggs!
              """))
        input("(Press ENTER to continue)")

        print(dedent("""
           Tokiwa: To make sure we're on the same page about the setup:
                   1) I'll stand with my bucket on the west side of the coop and you'll
                      be on the east side with your bucket.
                   2) There are 2 rows of 6 hens -- the nests on the southern side are
                      your playing field, while the northern nests are where I move. Each
                      hen has 4 eggs in her nest at the moment.
                   3) The goal is to gather as many eggs in your bucket as you can. The 
                      person with the most eggs wins!
              """))
        input("(Press ENTER to continue)")
        
        print(dedent("""
           Tokiwa: To make sure we're on the same page about the rules:
                   1) On each of our turns, we can choose one of the hen's nests. Each
                      of the eggs in the selected nest will be evenly distributed to the
                      dishes to their right (and so on, in the counter-clockwise direction).
                   2) Free moves: if you make a move and the last egg falls in your bucket, 
                      you get a free turn.
                   3) Capture: if the last egg for your move lands in an empty nest on your
                      side, then you can put that egg and any eggs in the opposite nest (so
                      one of mine :O ) in your bucket.
                   4) Game ends when all six nests on either your half or mine are empty. All
                      remaining eggs in nests on the non-empty side will be added to that side's
                      bucket.
              """))

        input("(Press ENTER to continue)")

        print(dedent("""
           Tokiwa: Whew, that was a lot, I hope this all makes sense! Let's play!!
                   You can go ahead and start.
              """))
        input("(Press ENTER to continue)")

        self.print_board()

        # Mancala!
        while not self.huilin_won:

            # Check if at end condition -- and whether we should end
            if self.check_end_condition():
                # Calc final scores
                self.tokiwas_bucket += sum(self.board[0])
                self.huilins_bucket += sum(self.board[1])
                print(f"Tokiwa: And that's the game! I've got {self.tokiwas_bucket} and you've got {self.huilins_bucket}.")

                # Tokiwa won
                if self.tokiwas_bucket > self.huilins_bucket:
                    print("Tokiwa: WOOHOO I won!! I wanna play again!! Let's put the eggs back and restart!")
                # Tie
                elif self.tokiwas_bucket == self.huilins_bucket:
                    print(dedent("""
                        Tokiwa: We tied! Aww that's no fun, only one of us can be the true winner 😤
                                Let's put the chicken eggs back and have a rematch!
                    """))
                # Huilin won
                else:
                    print("Tokiwa: Nice, you won! Thanks for playing with me!")
                    self.huilin_won = True
                    break

                # Reset
                self.board = [ [4 for i in range(6)] for j in range(2) ]
                self.tokiwas_bucket = 0
                self.huilins_bucket = 0
                self.huilins_turn = True
                self.print_board()
                input("(Press ENTER to continue)")
                continue

            # Move if Tokiwa
            if not self.huilins_turn:
                print("It's Tokiwa's turn...")
                time.sleep(2)
                self.tokiwas_move()
                print("Tokiwa made his move.")
            
            # Huilin's move!
            else:
                user_quit = None
                while user_quit != 'q':
                    try:
                        input_nest_idx, user_quit = self.input_exitable("Which nest do you choose? (Enter 0 thru 5, or q to exit): ")
                        if user_quit:
                            # Reset
                            self.board = [ [4 for i in range(6)] for j in range(2) ]
                            self.tokiwas_bucket = 0
                            self.huilins_bucket = 0
                            self.huilins_turn = True
                            return
                        nest_idx = int(input_nest_idx)
                        if nest_idx < 0 or nest_idx > 5 or self.board[1][nest_idx] == 0:
                            print("Invalid input, try again")
                            continue
                        free_turn = self.move_eggs(nest_idx)
                        self.huilins_turn = free_turn
                        break
                    except:
                        pass

                
            self.print_board()

        
        self.stats.update_strength(1)
        self.stats.update_stamina(-1)
        self.stats.print_stats()
        self.completed = True

    # Helper functions
    def move_eggs(self, idx):

        # Track 4 things: idx, row, num eggs, whose turn (class var)
        curr_idx = idx
        if self.huilins_turn:
            curr_row = 1
        else:
            curr_row = 0
        num_eggs = self.board[curr_row][curr_idx]
        self.board[curr_row][curr_idx] = 0
        free_turn = False
        
        # Move the actual eggs, movement is based on row
        while num_eggs:

            # Huilin's
            if curr_row:
                # At the edge -- add to bucket
                if curr_idx == 5:
                    if self.huilins_turn:
                        print("You added an egg to your bucket!")
                        self.huilins_bucket += 1
                        # Free turn
                        if num_eggs == 1:
                            free_turn = True
                            print("Huilin gets a free turn!")
                    curr_row = 0
                    curr_idx = 6
                # If anywhere else
                else:
                    # Captures - Huilin's side
                    next_idx = curr_idx + 1
                    if self.huilins_turn and num_eggs == 1 and self.board[1][next_idx] == 0 and self.board[0][next_idx] > 0:
                        self.huilins_bucket += 1 + self.board[0][next_idx]
                        self.board[0][next_idx] = 0
                        print("Huilin captures!")

                    # Otherwise just add to the next row
                    else:
                        self.board[curr_row][next_idx] += 1

                    curr_idx += 1

            # Tokiwa's side
            else:
                # At the edge -- add to bucket
                if curr_idx == 0:
                    if not self.huilins_turn:
                        print("Tokiwa added an egg to his bucket!")
                        self.tokiwas_bucket += 1
                        # Free turn
                        if num_eggs == 1:
                            free_turn = True
                            print("Tokiwa gets a free turn!")
                    curr_row = 1
                    curr_idx = -1
                # If anywhere else
                else:
                    # Captures - Tokiwa's side
                    next_idx = curr_idx - 1
                    if not self.huilins_turn and num_eggs == 1 and self.board[0][next_idx] == 0 and self.board[1][next_idx] > 0:
                        self.tokiwas_bucket += 1 + self.board[1][next_idx]
                        self.board[1][next_idx] = 0
                        print("Tokiwa captures!")

                    # Otherwise just add to the next row
                    else:
                        self.board[curr_row][next_idx] += 1

                    curr_idx -= 1

            num_eggs -= 1
        
        return free_turn

    def tokiwas_move(self):

        # Choose any of the 6 moves randomly, so long as it's valid
        nest_idx = None
        while nest_idx == None:
            select = random.randrange(0, 6)
            if self.board[0][select] != 0:
                nest_idx = select
        
        # Now move the eggs
        free_turn = self.move_eggs(nest_idx)

        self.huilins_turn = not free_turn


    def check_end_condition(self):
        
        # Check if either are empty
        tokiwa_empty = sum(self.board[0]) == 0
        huilin_empty = sum(self.board[1]) == 0

        return tokiwa_empty or huilin_empty

    def print_board(self):
        print("\nBucket locations are represented with first initials -- totals shown below.")
        tokiwas_str = [ str(val) for val in self.board[0]]
        huilins_str = [ str(val) for val in self.board[1]]
        labels = [ str(i) for i in range(6) ]
        print("T |", " | ".join(tokiwas_str), "| H")
        print("  |", " | ".join(huilins_str), "|  ")
        print("   ", "   ".join(labels), "   ")

        print("Tokiwa's score:", self.tokiwas_bucket)
        print("Huilin's score:", self.huilins_bucket)

        print()
