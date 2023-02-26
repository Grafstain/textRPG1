class Enemy:
    """
    This class represents an enemy that a character can fight.

    An enemy has a name, a level, and a set of attributes (e.g. strength,
    dexterity, and intelligence) that determine its combat abilities.

    Attributes:
        name (str): The name of the enemy.
        level (int): The level of the enemy.
        attributes (dict): A dictionary of the enemy's attributes and
            their values (e.g. {"strength": 10, "dexterity": 5, "intelligence": 3}).
    """

    def __init__(self, name, level, attributes):
        """
        Creates a new Enemy object with the given name, level, and attributes.

        Args:
            name (str): The name of the enemy.
            level (int): The level of the enemy.
            attributes (dict): A dictionary of the enemy's attributes and
                their values (e.g. {"strength": 10, "dexterity": 5, "intelligence": 3}).
        """
        self.name = name
        self.level = level
        self.attributes = attributes
