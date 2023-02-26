class World:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def game_loop(self):
        print("Welcome to the Text RPG game!")
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"{self.player.name}: Health = {self.player.health}, Mana = {self.player.mana}")
            print(f"{self.enemy.name}: Health = {self.enemy.health}")

            action = input("What would you like to do? (a)ttack, (u)se item: ")

            if action == "a":
                self.player.attack(self.enemy)
                if not self.enemy.is_alive():
                    print(f"{self.enemy.name} has been defeated!")
                    break
                self.enemy.attack(self.player)
                if not self.player.is_alive():
                    print("You have been defeated!")
                    break

            elif action == "u":
                if not self.player.items:
                    print("You have no items!")
                    continue
                print("Your items:")
                for i, item in enumerate(self.player.items):
                    print(f"{i + 1}: {item.name}")
                choice = input("Choose an item to use: ")
                try:
                    index = int(choice) - 1
                    item = self.player.items[index]
                    item.use(self.player)
                    self.player.items.pop(index)
                except (ValueError, IndexError):
                    print("Invalid choice!")
                    continue
                self.enemy.attack(self.player)
                if not self.player.is_alive():
                    print("You have been defeated!")
                    break

        if self.player.is_alive():
            print("You win!")
        else:
            print("You lose!")
