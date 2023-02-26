# create a new character and allocate attribute points
from character import Character
from enemy import Enemy
from world import World

player = Character("Player", 10, 5, 5)
print("Allocating attribute points...")
while True:
    try:
        health_points = int(input("How many points do you want to allocate to health? "))
        strength_points = int(input("How many points do you want to allocate to strength? "))
        defense_points = int(input("How many points do you want to allocate to defense? "))
        player.allocate_attributes(health_points, strength_points, defense_points)
        break
    except ValueError as e:
        print(e)

# create a new enemy
enemy = Enemy("Enemy", 10, 5)

# create a new game world
world = World(player, enemy)

# start the game loop
world.game_loop()
