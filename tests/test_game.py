import unittest
from character import Character
from enemy import Enemy
from item import Item
from game import Game


class GameTest(unittest.TestCase):
    """
    This class contains test cases for the Game class.

    Each test case verifies that a different method or attribute of
    the Game class works as expected.
    """

    def test_init(self):
        """
        This test case verifies that the __init__ method correctly
        initializes a new Game object.

        It does this by creating a new Game object with known
        attribute values and verifying that the object's attributes
        have the expected values.
        """
        player = Character("Test Player", 10, 5, 100)
        enemies = [Enemy("Test Enemy", 1, 10, 100)]
        items = [Item("Test Item", "description", "attribute", 10)]
        game = Game(player, enemies, items)
        self.assertEqual(game.player, player)
        self.assertEqual(game.enemies, enemies)
        self.assertEqual(game.items, items)

    def test_battle(self):
        """
        This test case verifies that the battle method correctly
        simulates a turn-based battle between the player and an enemy.

        It does this by creating a new Game object with a player and an
        enemy, and calling the battle method. The test verifies that the
        player and enemy take turns attacking each other until one of them
        is defeated.
        """
        player = Character("Test Player", 10, 5, 100)
        enemy = Enemy("Test Enemy", 1, 10, 100)
        game = Game(player, [enemy], [])
        game.battle(enemy)
        self.assertFalse(enemy.is_alive())
        self.assertTrue(player.is_alive())

    def test_start(self):
        """
        This test case verifies that the start method correctly
        starts the game loop and simulates battles and item collection.

        It does this by creating a new Game object with a player, enemies,
        and items, and calling the start method. The test verifies that the
        player fights all enemies and collects all items, and that the game
        ends when all enemies are defeated or the player dies.
        """
        player = Character("Test Player", 10, 5, 100)
        enemies = [Enemy("Test Enemy", 1, 10, 100)]
        items = [Item("Test Item", "description", "attribute", 10)]
        game = Game(player, enemies, items)
        game.start()
        self.assertFalse(game.enemies)
        self.assertFalse(game.items)
        self.assertTrue(player.is_alive())
