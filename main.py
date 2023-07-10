import time
from stats import Stats
from puzzles.m_horse_care import HorseCare
from puzzles.m_race_track import RaceTrack
from puzzles.m_aki_talk import AkiTalk
from puzzles.m_horse_ride import HorseRide
from puzzles.a_lunch import Lunch
from puzzles.a_pig_pen import PigPen
from puzzles.a_hachiken_talk import HachikenTalk
from puzzles.e_chicken_eggs import ChickenEggs
from puzzles.e_horse_manure import HorseManure
from puzzles.e_tokiwa_talk import TokiwaTalk
from puzzles.n_komaba_talk import KomabaTalk
from puzzle_set import PuzzleSet
from textwrap import dedent
from playsound import playsound

# Stats tracking vars
# Instantiated here, read from file
stats = Stats()

# Welcome code
print(dedent("""
         It's been a long day.

         Happy, but long -- and maybe kind of stressful. Working a full time job, finishing 
         up a Masters thesis, and making the most of the summer isn't easy! 
         
         As you climb into bed and drift off to sleep, you can't help but wonder if you could 
         have a break from it all... a simpler life, even for just a little bit...

         Maybe even on a farm...

         zzzzzzzzzzz
              """))
input("(Press ENTER to continue)")

time.sleep(2)
print(dedent("""
         ???: WAKE UP!
              """))

input("(Press ENTER to continue)")

print(dedent("""
         Aki: Ah, sorry! I didn't mean to scare you -- you're a pretty deep sleeper! I 
              wanted to make sure you got up on time, since I know this is your first day
              here. Don't hesitate to ask if you have any questions, and see you at breakfast!
              """))

input("(Press ENTER to continue)")

print(dedent("""
         While trying to shake the grogginess, you can sort of recognize the girl as she
         runs off to breakfast -- that's Aki, right?
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
         Go on! The wonderful world of agriculture awaits (breakfast too~)!
              """))

input("(Press ENTER to continue)")

stats.print_stats()

input("(Press ENTER to continue)")

time.sleep(2)

print(dedent("""
         Aki: Hi!! I'm so glad you found your way to breakfast before it ended.
              Everyone's heading off to do this morning's chores, and it looks like
              we've been assigned to the horses! Do you like horses at all? 
              """))

# TODO: validate -- not that it matters, but catching non 1-3 input
input(dedent("""
         1) Yes!!
         2) Abso-friggin-lutely!!!!
         3) 🐴
         
              """))

print(dedent("""
         Aki: Ohhh, great!! Let me take you to the horses then!
              """))

input("(Press ENTER to continue)")

# Puzzle Set 1 - Morning
    # Update the global stats object
morning_intro = dedent("""
         Aki: So... this is the horse pen. It's a lot of work to take care of the horses, 
              but taking care of the horses makes riding them even more special. It looks like
              we've been tasked with feeding the horses and setting up a horse race track.
              """)
horse_care = HorseCare(stats, False)
race_track = RaceTrack(stats, False)
aki_talk = AkiTalk(stats, False)
morning = PuzzleSet(stats, [horse_care,race_track,aki_talk], introduction=morning_intro)
if not morning.set_complete:
    stats = morning.run()

# Puzzle - Horse Riding Event
horse_riding = HorseRide(stats, False) 
if morning.set_complete and not horse_riding.completed:
    horse_riding.puzzle()

# Puzzle Set 2 - Afternoon
afternoon_intro = dedent("""
    Hachiken: Hi Huilin san! Nice to meet you. It seems like you and I have been paired 
              for chores until lunch! We've been assigned to the pigs and making pizza
              for lunch.
              """)

lunch = Lunch(stats, False)
pig_pen = PigPen(stats, False)
hachiken_talk = HachikenTalk(stats, False)
afternoon = PuzzleSet(stats, [pig_pen,lunch,hachiken_talk], introduction=afternoon_intro)
if horse_riding.completed and not afternoon.set_complete:
    stats = afternoon.run()

# Puzzle - Baseball
baseball_puzzle_complete = False # TODO: make actual obj
if afternoon.set_complete and not baseball_puzzle_complete:
    print("TODO")

# Puzzle Set 3 - Evening
evening_intro = dedent("""
    Tokiwa: Hiya! Looks like we're assigned to work together for the evening shift!
            Ready for some winner winner chicken pre-dinner? And by that I mean, we (both 
            key players on the WINNING baseball team, haha!) have been assigned to the 
            chickens for pre-dinner chores. 
            ...
            (We also have to dig up manure, but I'm going to ignore that for now.)
              """)
chicken_eggs = ChickenEggs(stats, False)
horse_manure = HorseManure(stats, False)
tokiwa_talk = TokiwaTalk(stats, False)
evening = PuzzleSet(stats, [chicken_eggs, horse_manure, tokiwa_talk], introduction=evening_intro)
if baseball_puzzle_complete and not evening.set_complete:
    stats = evening.run()


# Talk with Komaba
komaba_talk = KomabaTalk(stats,False)
if evening.set_complete and not komaba_talk.completed:
    print(dedent("""
        Having finished all of your evening chores, you decide to wander around campus a bit. As
        you look at the setting sun you think of what a long day it has been - long but 
        fulfilling... 
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        Wait... didn't I have that thought before? ... It was right before I went to sleep...
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        I'm dreaming, you realize, and you feel yourself waking up. Wait, no I'm not done with
        everything... there's still one more thing I have to do.
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        The thought of him makes him arrive. You see Komaba kun jogging over to you holding a baseball
        in one hand and a picture of his family in the other.
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        As he approaches you he tucks the picture and the baseball into his pocket.
        Komaba: Hey Huilin, glad I got to see you before you went off to bed. I just wanted to
                thank you for cracking the other teams baseball signs. I never thought it was
                possible. You'll have to teach me how you did it. It will be useful when I 
                uhh... 
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        Huilin: When you play baseball in the US!
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        Komaba: IF I play baseball in the US... Tokiwa told you?
    """))
    input("(Press ENTER to continue)")
    print(dedent("""
        Huilin: Yup! Well anyways, the baseball signs weren't actually that hard to crack. I have 
                a friend who's been training me to break codes like that. I can definately teach 
                you how to do it, but first I actually wanted to talk to you about some other things...
    """))
    stats = komaba_talk.run()
# Wrap Up
if komaba_talk.completed:
    print("\nYou head off towards the girls dormitory guided by the light of the full moon.\n")
    input("(Press ENTER to continue)")
    print('As you drift off to sleep you think: "I\'m going to miss this place" ')
# Save and exit
# print("Game has been saved.")
# TODO: write to the file here