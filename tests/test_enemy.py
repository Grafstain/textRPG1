import unittest
from enemy import Enemy


class EnemyTest(unittest.TestCase):
    """
    This class contains test cases for the Enemy class.

    Each test case verifies that a different method or attribute of
    the Enemy class works as expected.
    """

    def test_init(self):
        """
        This test case verifies that the __init__ method correctly
        initializes a new Enemy object.

        It does this by creating a new Enemy object with known
        attribute values and verifying that the object's attributes
        have the expected values.
        """
        attributes = {"strength": 10, "dexterity": 5, "intelligence": 3}
        enemy = Enemy("Goblin", 1, attributes)
        self.assertEqual(enemy.name, "Goblin")
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy.attributes, attributes)


if __name__ == '__main__':
    unittest.main()
