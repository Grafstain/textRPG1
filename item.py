class Item:
    """
    This class represents an item that can be used by a character.

    An item has an effect and an amount. The effect determines what
    attribute the item modifies (e.g. strength, dexterity, or
    intelligence) and the amount determines how much the attribute
    is modified by.

    Attributes:
        effect (str): The effect of the item (e.g. "strength").
        amount (int): The amount by which the effect modifies the
            character's attribute.
    """

    def __init__(self, effect, amount):
        """
        Creates a new Item object with the given effect and amount.

        Args:
            effect (str): The effect of the item (e.g. "strength").
            amount (int): The amount by which the effect modifies the
                character's attribute.
        """
        self.effect = effect
        self.amount = amount
