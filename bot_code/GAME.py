class Game:
    def __init__(self):
        self.filter: bool = False
        self.complete: list = [False, "none"]
        self.score: int = 0

    def add_score(self):
        self.score += 10

    def add_player(self, id, name):
        with open("Players.txt", "w", encoding='utf-8') as myfile:
            myfile.write(f"{name} - {id}\n")
