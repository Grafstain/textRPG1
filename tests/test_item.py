import unittest
from item import Item

class ItemTest(unittest.TestCase):
    """
    This class contains test cases for the Item class.

    Each test case verifies that a different method or attribute of
    the Item class works as expected.
    """

    def test_init(self):
        """
        This test case verifies that the __init__ method correctly
        initializes a new Item object.

        It does this by creating a new Item object with known
        attribute values and verifying that the object's attributes
        have the expected values.
        """
        item = Item("strength", 5)
        self.assertEqual(item.effect, "strength")
        self.assertEqual(item.amount, 5)

if __name__ == '__main__':
    unittest.main()
