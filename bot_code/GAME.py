import re
class Game:
    def __init__(self):
        self.filter: bool = False
        self.complete: list = [False, "none"]
        self.score: int = 0
    def add_score(self, id):
        with open('Players.txt') as f:
            lines = f.readlines()
        str = id
        pattern = re.compile(re.escape(str))
        with open('Players.txt', 'w') as f:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    f.write(line)



    def add_player(self, id, name):
        with open("Players.txt", "w") as myfile:
            myfile.write(f"{name} - {id} - {self.score}\n")
