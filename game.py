from character import Character
from enemy import Enemy
from item import Item


class Game:
    """
    This class represents a text-based RPG game.

    The game consists of a player character, a series of enemies that
    the player must defeat, and a set of items that the player can
    collect to help them in their quest.

    Attributes:
        player (Character): The player's character.
        enemies (list): A list of Enemy objects that the player must defeat.
        items (list): A list of Item objects that the player can collect.
    """

    def __init__(self, player, enemies, items):
        """
        Creates a new Game object with the given player character, list of
        enemies, and list of items.

        Args:
            player (Character): The player's character.
            enemies (list): A list of Enemy objects that the player must defeat.
            items (list): A list of Item objects that the player can collect.
        """
        self.player = player
        self.enemies = enemies
        self.items = items

    def start(self):
        """
        Starts the game.

        This method starts the game loop, which consists of the player
        fighting enemies and collecting items until all enemies are defeated
        or the player dies.
        """
        print("Welcome to the Text RPG Game!")
        print("You are playing as {}".format(self.player.name))

        while self.player.is_alive() and self.enemies:
            enemy = self.enemies[0]
            print("You are fighting a {} (Level {})".format(enemy.name, enemy.level))
            self.battle(enemy)
            if not self.player.is_alive():
                print("You have died. Game over.")
                return
            else:
                self.enemies.pop(0)

        print("Congratulations! You have defeated all enemies and won the game.")

    def battle(self, enemy):
        """
        Simulates a battle between the player and an enemy.

        This method simulates a turn-based battle between the player and
        the given enemy. The player and the enemy take turns attacking
        each other until one of them is defeated.

        Args:
            enemy (Enemy): The enemy that the player is fighting.
        """
        while self.player.is_alive() and enemy.is_alive():
            # Player's turn
            player_damage = self.player.attack()
            print("You deal {} damage to the {}.".format(player_damage, enemy.name))
            enemy.take_damage(player_damage)
            if not enemy.is_alive():
                print("You have defeated the {}!".format(enemy.name))
                self.player.gain_experience(enemy.level * 100)
                self.player.heal(10)
                return

            # Enemy's turn
            enemy_damage = enemy.attack()
            print("The {} deals {} damage to you.".format(enemy.name, enemy_damage))
            self.player.take_damage(enemy_damage)
            if not self.player.is_alive():
                return
