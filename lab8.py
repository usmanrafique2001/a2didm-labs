import random

def play(rounds, knows_password):
    for _ in range(rounds):
        peggy_side = random.choice(["left", "right"])
        victor_shouts = random.choice(["left", "right"])
        if peggy_side != victor_shouts and not knows_password:
            return False        # bluffer stuck on the wrong side
    return True                 # passed every round

tries = 100000

honest = sum(play(10, True) for _ in range(tries))
print("honest Peggy passes 10 rounds:", honest, "out of", tries)

for rounds in [1, 2, 10, 20]:
    wins = sum(play(rounds, False) for _ in range(tries))
    print(f"bluffer passes {rounds} rounds:", wins, "out of", tries)
