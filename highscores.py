import json
import requests    #This module, not written by us, is used for communication with a server. The high scores are saved on a server.

class HighScores:    #This class figures out which scores are high scores, and sorts them into the appropriate order.

    # HighScores constructor 
    def __init__(self):
        self.scores = []    #Create an array into which scores can be placed.

    def retrieveData():     #This method gets JSON data from the server.
        """
        - returns JSON dictionary from our server
        """
        try:
            r = requests.get("http://128.226.244.161/data.json", timeout=10)    #If the server is online, then get the data.
        except requests.ConnectTimeout:
            print("Sorry, our servers are down.")                               #If the server is offline, then fail to get the data, and deliver a message to the user informing him that the server is offline.
        else:
            return r.json()    #If the server is online and the data are received successfully, then return the data in JSON format.

    def outputData(self):      #This method receives the score data from the code in gui.py, and inserts it into an array. The array is mutable, so the order of the scores can be changed in order to arrange the high scores.
        """
        - returns a sorted array of tuples (name, score)
        """
        scoresDict = HighScores.retrieveData()

        for i in scoresDict:
            self.scores.append((i, scoresDict[i]))

        return sorted(self.scores, key=lambda tup: int(tup[1]))    #This sorts the scores and organizes them.

    def addData(self, name, score):    #This method adds the new sorted data (in JSON format) to another array, which is given to the rest of the program for use in displaying the high scores.
        """
        - adds new data to the JSON file
        """
        arg = {"name": name, "score": score}

        try:
            r = requests.get("http://128.226.244.161/leaderboards.py", params=arg, timeout=10)    #If the server is online, then get the data.
        except requests.ConnectTimeout:
            print("Sorry, our servers are down.")                                                 #If the server is offline, then fail to get the data, and deliver a message to the user informing him that the server is offline.
