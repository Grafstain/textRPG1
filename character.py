class Character:
    """
    This class represents a character in the game.

    Attributes:
        name (str): The name of the character.
        strength (int): The strength attribute of the character.
        defense (int): The defense attribute of the character.
        health (int): The health attribute of the character.
        inventory (list): A list of the items currently held by the character.
        effects (dict): A dictionary of the effects currently applied to the character.
    """

    def __init__(self, name, strength, defense, health):
        """
        Initializes a new Character object with the specified name, strength,
        defense, and health attributes.

        Args:
            name (str): The name of the character.
            strength (int): The strength attribute of the character.
            defense (int): The defense attribute of the character.
            health (int): The health attribute of the character.
        """
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health
        self.inventory = []
        self.effects = {}

    def take_damage(self, damage):
        """
        Causes the character to take the specified amount of damage.

        Args:
            damage (int): The amount of damage to inflict on the character.
        """
        self.health -= damage

    def is_alive(self):
        """
        Determines whether the character is alive or dead.

        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.health > 0

    def add_item(self, item):
        """
        Adds the specified item to the character's inventory.

        Args:
            item (Item): The item to add to the character's inventory.
        """
        self.inventory.append(item)

    def remove_item(self, item):
        """
        Removes the specified item from the character's inventory.

        Args:
            item (Item): The item to remove from the character's inventory.
        """
        self.inventory.remove(item)

    def add_effect(self, effect):
        """
        Adds the specified effect to the character.

        Args:
            effect (Effect): The effect to add to the character.
        """
        self.effects[effect.name] = effect

    def remove_effect(self, effect):
        """
        Removes the specified effect from the character.

        Args:
            effect (Effect): The effect to remove from the character.
        """
        del self.effects[effect.name]

    def attack_enemy(self, enemy):
        """
        Causes the character to attack the specified enemy.

        Args:
            enemy (Enemy): The enemy to attack.
        """
        damage = self.strength - enemy.defense
        if damage > 0:
            enemy.take_damage(damage)
        return damage
