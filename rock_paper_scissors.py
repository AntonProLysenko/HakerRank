import random
class RockPaperScisors():
    variants={
        "rock":1,
        "paper":2,
        "scisors":3
    }



class Player():
    def __init__(self,name:str) -> None:
        self.name=name

    def play_single_game(self,variants):
        print(variants)
        print("in Ganme")
        computer_variant = random.choice(list(variants.items()))
        player_variant = random.choice(list(variants.items()))
        print(f"{computer_variant}")
        print(f"{player_variant}")
        if computer_variant == variants["scisors"] and player_variant == variants["rock"]:
            print(f"{self.name} Won!")
        elif computer_variant == variants["rock"] and player_variant == variants["scisors"]:
            print("Machine beats Human")
        # return FingerGame.variants
        


rock_paper_scissors = RockPaperScisors()
player1 = Player("Palyer1")

print(player1.play_single_game(rock_paper_scissors.variants))



