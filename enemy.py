from character import Character


class Enemy(Character):
    """
    Represents an enemy character in the game.
    """

    def __init__(self, name, attributes=None, health=100):
        """
        Initializes a new enemy character with the specified name, attributes, and health.

        :param name: The name of the enemy character.
        :param attributes: A dictionary of attributes that the enemy character has.
        :param health: The starting health of the enemy character.
        """
        super().__init__(name, attributes=attributes, health=health)

    def attack(self, character):
        """
        Attacks the specified character.

        :param character: The character to attack.
        """
        damage = self.attributes["strength"] - character.attributes["defense"]
        character.health -= damage
