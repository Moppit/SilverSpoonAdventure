import time
from stats import Stats
from puzzles.m_horse_care import HorseCare
from puzzle_set import PuzzleSet
from textwrap import dedent

# Stats tracking vars
# Instantiated here, read from file
stats = Stats()

# Welcome code
print(dedent("""
         It's been a long day.\n

         Happy, but long -- and maybe kind of stressful. Working a full time job, finishing \n
         up a Masters thesis, and making the most of the summer isn't easy! \n
         
         As you climb into bed and drift off to sleep, you can't help but wonder if you could \n
         have a break from it all... a simpler life, even for just a little bit...\n

         Maybe even on a farm...\n

         zzzzzzzzzzz
              """))

input("(Press ENTER to continue)")

time.sleep(2)
print(dedent("""
         ???: WAKE UP!
              """))

input("(Press ENTER to continue)")

print(dedent("""
         Aki: Ah, sorry! I didn't mean to scare you -- you're a pretty deep sleeper! I \n
              wanted to make sure you got up on time, since I know this is your first day\n
              here. Don't hesitate to ask if you have any questions, and see you at breakfast!\n
              """))

input("(Press ENTER to continue)")

print(dedent("""
         While trying to shake the grogginess, you can sort of recognize the girl as she\n
         runs off to breakfast -- that's Aki, right?\n
              """))

input("(Press ENTER to continue)")

print("""
                Welcome to the world of...
         _   _   _   _   _   _     _   _   _   _   _  
        / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ 
       ( S | i | l | v | e | r ) ( S | p | o | o | n )
        \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ 
      """)

print(dedent("""
         Go on! The wonderful world of agriculture awaits (breakfast too~)!\n
              """))

input("(Press ENTER to continue)")

time.sleep(2)

print(dedent("""
         Aki: Hi!! I'm so glad you found your way to breakfast before it ended.\n
              Everyone's heading off to do this morning's chores, and it looks like\n
              we've been assigned to the horses! Do you like horses at all?\n
              """))

# TODO: validate -- not that it matters, but catching non 1-3 input
input(dedent("""
         1) Yes!!\n
         2) Abso-friggin-lutely!!!!\n
         3) 🐴\n
              """))

print(dedent("""
         Aki: Ohhh, great!! Let me take you to the horses then!
              """))

input("(Press ENTER to continue)")

# Puzzle Set 1 - Morning
    # Update the global stats object
morning_intro = dedent("""
         Aki: So... this is the horse pen. It's a lot of work to take care of the horses, \n
              but taking care of the horses makes riding them even more special. It looks like\n
              we've been tasked with feeding the horses and setting up a horse race track.
              """)
horse_care = HorseCare(stats, False)
morning = PuzzleSet(stats, [horse_care,horse_care,horse_care], introduction=morning_intro)
if not morning.set_complete:
    stats = morning.run()

# Puzzle - Horse Riding Event
horse_riding_puzzle_complete = True # TODO: make actual obj
if morning.set_complete and not horse_riding_puzzle_complete:
    print("TODO")

# Puzzle Set 2 - Afternoon
afternoon = PuzzleSet(stats, [horse_care,horse_care,horse_care])
if horse_riding_puzzle_complete and not afternoon.set_complete:
    print("TODO")

# Puzzle - Baseball

# Puzzle Set 3 - Evening

# Talk with Komaba

# Wrap Up

# Save and exit
print("Game has been saved.")
# TODO: write to the file here