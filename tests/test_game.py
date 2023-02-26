import unittest
from character import Character
from enemy import Enemy
from item import Item
from game import Game


class GameTest(unittest.TestCase):
    """
    This class contains the unit tests for the Game class.
    """

    def setUp(self):
        """
        Initializes a new Game object and adds enemies and items to it.
        """
        self.player = Character("Test Player", 100, {"strength": 10})
        self.enemy = Enemy("Test Enemy", 50, {"strength": 5}, 10)
        self.item = Item("Test Item", "An item for testing", {"strength": 2})
        self.game = Game(self.player, [self.enemy], [self.item])

    def test_add_enemy(self):
        """
        Tests that an enemy can be added to the game.
        """
        new_enemy = Enemy("New Enemy", 50, {"strength": 5}, 10)
        self.game.add_enemy(new_enemy)
        self.assertIn(new_enemy, self.game.enemies)

    def test_add_item(self):
        """
        Tests that an item can be added to the game.
        """
        new_item = Item("New Item", "Another item for testing", {"strength": 3})
        self.game.add_item(new_item)
        self.assertIn(new_item, self.game.items)

    def test_play_turn(self):
        """
        Tests that a turn can be played in the game.
        """
        self.assertTrue(self.game.play_turn())
