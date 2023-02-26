class Enemy:
    """
    This class represents an enemy in the game.

    Attributes:
        name (str): The name of the enemy.
        strength (int): The strength attribute of the enemy.
        defense (int): The defense attribute of the enemy.
        health (int): The health attribute of the enemy.
    """

    def __init__(self, name, strength, defense, health):
        """
        Initializes a new Enemy object with the specified name, strength,
        defense, and health attributes.

        Args:
            name (str): The name of the enemy.
            strength (int): The strength attribute of the enemy.
            defense (int): The defense attribute of the enemy.
            health (int): The health attribute of the enemy.
        """
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def take_damage(self, damage):
        """
        Causes the enemy to take the specified amount of damage.

        Args:
            damage (int): The amount of damage to inflict on the enemy.
        """
        self.health -= damage

    def is_alive(self):
        """
        Determines whether the enemy is alive or dead.

        Returns:
            bool: True if the enemy is alive, False otherwise.
        """
        return self.health > 0

    def attack_character(self, character):
        """
        Causes the enemy to attack the specified character.

        Args:
            character (Character): The character to attack.
        """
        damage = self.strength - character.defense
        if damage > 0:
            character.take_damage(damage)
        return damage
