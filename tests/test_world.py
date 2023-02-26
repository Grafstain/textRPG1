import unittest
from contextlib import redirect_stdout

from character import Character
from enemy import Enemy
from item import Item
from game import Game
from world import World


class TestWorld(unittest.TestCase):
    """
    Test class for the World class.
    """

    def test_play(self):
        """
        Tests the play method of the World class.
        """
        player_attributes = {"strength": 10, "defense": 5, "intelligence": 2}
        player = Character("Player", attributes=player_attributes)

        enemy_attributes = {"strength": 5, "defense": 2, "intelligence": 1}
        enemy = Enemy("Enemy", attributes=enemy_attributes)

        world = World(player, enemy)

        # Test that the game ends when one character's health reaches zero
        with unittest.mock.patch('builtins.input', side_effect=["1", "1"]):
            with io.StringIO() as buf, redirect_stdout(buf):
                world.play()
                output = buf.getvalue()
                self.assertIn("You win!", output)

        player.health = 1

        with unittest.mock.patch('builtins.input', side_effect=["1", "1"]):
            with io.StringIO() as buf, redirect_stdout(buf):
                world.play()
                output = buf.getvalue()
                self.assertIn("You lose.", output)
