class Character:
    """
    Represents a character in the game.

    Attributes:
    - name: The name of the character.
    - strength: The character's strength attribute.
    - dexterity: The character's dexterity attribute.
    - intelligence: The character's intelligence attribute.
    """

    def __init__(self, name, strength, dexterity, intelligence):
        """
        Initializes a new character object with the given attributes.

        Arguments:
        - name: The name of the character.
        - strength: The character's strength attribute.
        - dexterity: The character's dexterity attribute.
        - intelligence: The character's intelligence attribute.
        """
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def attack(self):
        """
        Calculates the character's attack power based on their strength attribute.

        Returns:
        The character's attack power.
        """
        return self.strength

    def defend(self):
        """
        Calculates the character's defense power based on their dexterity attribute.

        Returns:
        The character's defense power.
        """
        return self.dexterity

    def use_item(self, item):
        """
        Applies the effect of the given item to the character.

        Arguments:
        - item: The item to use.

        Returns:
        None.
        """
        try:
            effect = item["effect"]
            amount = item["amount"]
        except KeyError:
            print("Error: Item is missing a required attribute.")
            return

        if effect == "strength":
            self.strength += amount
        elif effect == "dexterity":
            self.dexterity += amount
        elif effect == "intelligence":
            self.intelligence += amount
        else:
            print(f"Error: Invalid effect attribute {effect}.")

