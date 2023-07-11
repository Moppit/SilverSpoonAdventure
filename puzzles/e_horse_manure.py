from puzzle import Puzzle
import sys
import time
import random
from textwrap import dedent
sys.path.insert(0, './..')

class HorseManure(Puzzle):

    def __init__(self, stats, completed=False):
        super().__init__(stats, completed)
        self.description = "Scoop horse manure"
        self.save_key = "EHM"
        self.mine_locations = []
        self.width = 6
        self.num_mines = 5
        self.board = [] # width x width of [display, value]
        self.ascii_factor = 65
        self.symbols = {
            "covered": "⬜",
            "blank": "🟩",
            "marked": "⛳",
            "mine": "💩",
            "1": "1️⃣ ",  # note: keep the spaces, they are important because
            "2": "2️⃣ ",  #       some emojis take 2 spaces while others take 1.
            "3": "3️⃣ ",  #       The current setup gives each emoji 2 spaces
            "4": "4️⃣ ",
            "5": "5️⃣ ",
            "6": "6️⃣ ",
            "7": "7️⃣ ",
            "8": "8️⃣ "
        }

    def get_neighbors(self, row, col):
        deltas = [-1, 0, 1]
        neighbors = []
        for r_delta in deltas:
            for c_delta in deltas:
                if (r_delta or c_delta):
                    # Bounds check
                    r = row + r_delta
                    c = col + c_delta
                    if r >= 0 and r < self.width and c >= 0 and c < self.width:
                        neighbors.append((r, c))
        return neighbors

    def create_board(self):
        # Generate the mine locations
        self.board = []
        self.mine_locations = []
        num_mines_generated = 0
        while num_mines_generated < self.num_mines:
            row = random.randrange(0, self.width)
            col = random.randrange(0, self.width)
            if not (row, col) in self.mine_locations:
                self.mine_locations.append((row, col))
                num_mines_generated += 1

        # Create the board -- [display, value]
        for row in range(self.width):
            self.board.append([])
            for col in range(self.width):

                # Check mines in vicinity
                num_near = 0
                neighbors = self.get_neighbors(row, col)
                for neighbor in neighbors:
                    if neighbor in self.mine_locations:
                        num_near += 1

                value = None

                # Value: mine
                if (row, col) in self.mine_locations:
                    value = "mine"

                # Value: number -- how many mines it's next to
                elif num_near > 0: 
                    value = str(num_near)

                # Value: blank
                else:
                    value = "blank"

                self.board[row].append(["covered", value])

    def board_is_uncovered(self):
        count_marked = 0
        for row in self.board:
            for item in row:
                if item[0] == 'covered':
                    return False
                elif item[0] == 'marked':
                    count_marked += 1
        return count_marked == self.num_mines
    
    def print_board(self):
        # Print top axis
        print("  ", end="")
        for i in range(self.width):
            print(f"{i} ", end="")
        print()
        # Print emojis
        for row in range(self.width):
            print(f"{chr(row + self.ascii_factor)} ", end="")
            for col in range(self.width):
                print(self.symbols[self.board[row][col][0]], end="")
            print()

    def is_valid_tile(self, tile):
        if len(tile) != 2:
            return False
        valid_letter = tile[0] in [chr(i + self.ascii_factor) for i in range(self.width)]
        valid_number = tile[1] in [str(i) for i in range(self.width)]
        return valid_letter and valid_number

    def get_tile_coordinates(self, tile):
        row = ord(tile[0]) - self.ascii_factor
        col = int(tile[1])
        return row, col
    
    def get_tile_values(self, tile):
        row, col = self.get_tile_coordinates(tile)
        return self.board[row][col]

    def puzzle(self):
        print(dedent("""
           Tokiwa: Oof, manure. My least favorite part of this chore is...
                   ugh, finding crap in the open fields. I ALWAYS step on them.
                   Do you think you could mark the location of each of the piles 
                   of crap that you find? I'll come after you and scoop it all up, 
                   I just don't wanna risk, y'know... my shoes, and my sanity.
              """))

        input("(Press ENTER to continue)")

        print(dedent(f"""
           Tokiwa: Remember, there were only {self.num_mines} horses at the field today, so there should 
                   only be {self.num_mines} manure piles to mark. If you find yourself with more than {self.num_mines} marked spots,
                   be sure to narrow down the marked spots until you have the right amount!
              """))

        input("(Press ENTER to continue)")

        # Minesweeper!
        self.create_board()

        # Print legend
        print("----- LEGEND -----")
        print(self.symbols["covered"], "Unexplored spot")
        print(self.symbols["blank"], "Fresh, untainted grass")
        print(self.symbols["marked"], "Marked spot")
        print(self.symbols["mine"], "Horse crap")
        print(self.symbols["1"], "Number indicates how strong the smell is 🥲 1 is lowest")

        # Keep playing until all tiles are unlocked
        while not self.board_is_uncovered():

            # Display board
            self.print_board()

            try:
                # Get tile input
                tile, user_quit = self.input_exitable("Enter the tile to change (Ex: A2, or 'q' to quit): ")
                if user_quit:
                    return
                if self.is_valid_tile(tile) and self.get_tile_values(tile)[0] in ['covered', 'marked']:
                    actions = ['Uncover tile']
                    if self.get_tile_values(tile)[0] == 'marked':
                        actions.append('Un-flag tile')
                    else:
                        actions.append('Flag tile')
                    
                    # Ask user for action
                    for i in range(len(actions)):
                        print(i, actions[i])
                    action_input, user_quit = self.input_exitable("Choose an action (or 'q' to quit): ")
                    action = int(action_input)
                    if not action in [i for i in range(len(actions))]:
                        print("Action is invalid, please try again")
                    else:
                        # Execute the action!
                        r, c = self.get_tile_coordinates(tile)
                        if actions[action] == 'Uncover tile':
                            # It's a mine!!
                            if self.board[r][c][1] == 'mine':
                                print("Ack! You've stumbled upon some dung!")
                                dice_roll = random.randrange(0, 21)
                                if dice_roll < self.stats.dexterity:
                                    print("Luckily, your dexterity level was high enough to avoid it!")
                                    print("The spot has now been marked.")
                                    self.board[r][c][0] = 'marked'
                                else:
                                    print("Tough luck... you stepped in it 🥲")
                                    print(dedent("""
                                        Tokiwa: Yikes, did you step on some?? Sorry for making you do the dirty
                                                work, let's go back and get you cleaned up. We can come back and
                                                try this again later.
                                        """))
                                    self.board[r][c][0] = 'mine'
                                    self.print_board()
                                    input("(Press ENTER to continue)")
                                    return

                            # Not a mine
                            else:
                                self.board[r][c][0] = self.board[r][c][1]
                        elif actions[action] == 'Un-flag tile':
                            self.board[r][c][0] = 'covered'
                        elif actions[action] == 'Flag tile':
                            self.board[r][c][0] = 'marked'

                else:
                    print("Tile is invalid, please try again")

            except:
                pass
        
        # All tiles are uncovered and the correct number of tile are marked!
        self.print_board()
        print(dedent("""
           Tokiwa: You did it! Thanks so much! Now you can leave the scooping to me. :D
              """))

        input("(Press ENTER to continue)")
        
        self.stats.update_dexterity(3)
        self.stats.update_stamina(-1)
        self.stats.print_stats()
        self.completed = True
