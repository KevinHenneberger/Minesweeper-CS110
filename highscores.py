import json

class HighScores:

    # HighScores constructor 
    def __init__(self):
        self.scores = []

    def retrieveData():
        scoresFile = open("scores.json", "r")
        scoresDict = json.load(scoresFile)
        scoresFile.close()
        return scoresDict

    def outputData(self):
        scoresDict = HighScores.retrieveData()

        for i in scoresDict:
            self.scores.append((i, scoresDict[i]))

        return sorted(self.scores, key=lambda tup: tup[1])

    def addData(self, name, score):
        scoresDict = HighScores.retrieveData()
        scoresDict[name] = score
        scoresFile = open("scores.json", "w")
        json.dump(scoresDict, scoresFile)
        scoresFile.close()
