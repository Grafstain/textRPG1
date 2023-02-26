class Game:
    """
    This class represents the game.

    Attributes:
        player (Character): The player character in the game.
        enemies (list): A list of Enemy objects representing the enemies
                        in the game.
        items (list): A list of Item objects representing the items
                      available in the game.
    """

    def __init__(self, player, enemies=None, items=None):
        """
        Initializes a new Game object with the specified player, enemies,
        and items.

        Args:
            player (Character): The player character in the game.
            enemies (list): A list of Enemy objects representing the enemies
                            in the game. Defaults to an empty list if not
                            specified.
            items (list): A list of Item objects representing the items
                          available in the game. Defaults to an empty list if
                          not specified.
        """
        self.player = player
        self.enemies = [] if enemies is None else enemies
        self.items = [] if items is None else items

    def add_enemy(self, enemy):
        """
        Adds an enemy to the game.

        Args:
            enemy (Enemy): The enemy to add to the game.
        """
        self.enemies.append(enemy)

    def add_item(self, item):
        """
        Adds an item to the game.

        Args:
            item (Item): The item to add to the game.
        """
        self.items.append(item)

    def play_turn(self):
        """
        Executes a single turn of the game.

        Returns:
            bool: True if the player is still alive, False otherwise.
        """
        for enemy in self.enemies:
            damage = enemy.attack_character(self.player)
            print(f"{enemy.name} attacks {self.player.name} for {damage} damage.")
            if not self.player.is_alive():
                print(f"{self.player.name} has been defeated!")
                return False
        return True
