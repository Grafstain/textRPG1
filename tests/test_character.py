import unittest
from character import Character


class CharacterTest(unittest.TestCase):
    """
    This class contains test cases for the Character class.

    Each test case verifies that a different method of the Character
    class works as expected.
    """

    def setUp(self):
        """
        This method is called before each test case.

        It creates a new Character object that will be used in the
        test cases.
        """
        self.character = Character("Test Character", 10, 10, 10)

    def test_attack(self):
        """
        This test case verifies that the attack method returns the
        correct value.

        It does this by calling the attack method and comparing its
        return value to the expected value.
        """
        self.assertEqual(self.character.attack(), 10)

    def test_defend(self):
        """
        This test case verifies that the defend method returns the
        correct value.

        It does this by calling the defend method and comparing its
        return value to the expected value.
        """
        self.assertEqual(self.character.defend(), 10)

    def test_use_item_strength(self):
        """
        This test case verifies that the use_item method correctly
        modifies the character's strength attribute when given an
        item with the "strength" effect.

        It does this by calling the use_item method with an item
        that increases the character's strength attribute and
        comparing the attribute to the expected value.
        """
        item = {"effect": "strength", "amount": 5}
        self.character.use_item(item)
        self.assertEqual(self.character.strength, 15)

    def test_use_item_dexterity(self):
        """
        This test case verifies that the use_item method correctly
        modifies the character's dexterity attribute when given an
        item with the "dexterity" effect.

        It does this by calling the use_item method with an item
        that increases the character's dexterity attribute and
        comparing the attribute to the expected value.
        """
        item = {"effect": "dexterity", "amount": 5}
        self.character.use_item(item)
        self.assertEqual(self.character.dexterity, 15)

    def test_use_item_intelligence(self):
        """
        This test case verifies that the use_item method correctly
        modifies the character's intelligence attribute when given an
        item with the "intelligence" effect.

        It does this by calling the use_item method with an item
        that increases the character's intelligence attribute and
        comparing the attribute to the expected value.
        """
        item = {"effect": "intelligence", "amount": 5}
        self.character.use_item(item)
        self.assertEqual(self.character.intelligence, 15)


if __name__ == '__main__':
    unittest.main()
