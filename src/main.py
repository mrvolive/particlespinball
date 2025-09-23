class Game:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Starting game: {self.name}")

    def end(self):
        print(f"Ending game: {self.name}")


if __name__ == "__main__":
    game = Game("Adventure Quest")
    game.start()
    # Game logic would go here
    game.end()
