import json
import requests

class HighScores:

    # HighScores constructor 
    def __init__(self):
        self.scores = []

    def retrieveData():
        try:
            r = requests.get("http://128.226.244.161/data.json", timeout=10)
        except requests.ConnectTimeout:
            print("Sorry, our servers are down.")
        else:
            return r.json() # returns json dictionary from server

    def outputData(self):
        scoresDict = HighScores.retrieveData()

        for i in scoresDict:
            self.scores.append((i, scoresDict[i]))

        return sorted(self.scores, key=lambda tup: int(tup[1]))

    def addData(self, name, score):
        arg = {"name": name, "score": score}

        try:
            r = requests.get("http://128.226.244.161/leaderboards.py", params=arg, timeout=10)
        except requests.ConnectTimeout:
            print("Sorry, our servers are down.")
