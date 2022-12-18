import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    damage = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", damage, "points of damage. Current health is", playerhp)

    if playerhp > 30:
        continue

    print("You have low health. You've been teleported to nearest inn.")
    break
