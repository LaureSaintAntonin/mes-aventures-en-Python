# qui interagit avec qui ?
# qui fait quoi à qui ?

# Pierre Feuille Ciseau
# « Pierre, papier, ciseaux » est un jeu joué par deux participants.
# Le jeu est constitué de tours. Dans chaque tour, un participant choisit un symbole de pierre,
# de papier ou de ciseaux, et l’autre participant fait de même.
# Le gagnant du tour est alors déterminé en comparant les symboles choisis.
# Les règles du jeu établissent que la pierre l’emporte sur les ciseaux, que les ciseaux l’emportent sur le
# papier (ils le coupent) et que le papier l’emporte sur la pierre (il l’enveloppe).
# Le gagnant du tour reçoit un point. Le jeu se poursuit en autant de manches que les participants en conviennent.
# Le gagnant est le participant ayant le plus de points.


class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(
            "{name}, select rock, paper, scissor, lizard or spock : ".format(
                name=self.name
            )
        )
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2, "lizard": 3, "spock": 4}
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(
            "Round resulted in a {result}".format(result=self.getResultAsString(result))
        )

        if result > 0:
            p1.incrementPoint(),
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        p1_choice = p1.toNumericalChoice()
        p2_choice = p2.toNumericalChoice()
        return self.rules[p1_choice][p2_choice]

    def getResultAsString(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return (res[result],)

    def awardPoints(self):
        print("implement")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("ObiOne")
        self.secondParticipant = Participant("Yoda")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == "y":
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                "Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(
                    p1name=self.participant.name,
                    p1points=self.participant.points,
                    p2name=self.secondParticipant.name,
                    p2points=self.secondParticipant.points,
                )
            )
        self.determineWinner()
        self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)


game = Game()
game.start()
