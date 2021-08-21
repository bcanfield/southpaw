from pulp import *
import pandas as pd
import time
import json


class LinearGenerator():
    def __init__(self, pandasDataframe, salaryCap, playersPerLineup, scoreColumnName, numLineupsToGenerate):
        self.pandasDataframe = pandasDataframe
        self.salaryCap = salaryCap
        self.scoreColumnName = scoreColumnName
        self.playersPerLineup = playersPerLineup
        self.numLineupsToGenerate = numLineupsToGenerate

    def run(self):
        # with open(self.jsonDataFilePath, 'r') as myfile:
        #     data = myfile.read()
        # players = json.loads(data)

        players = list(self.pandasDataframe['name'])
        salaries = dict(zip(players, self.pandasDataframe['salary']))
        scores = dict(zip(players, self.pandasDataframe[self.scoreColumnName]))
        player_vars = LpVariable.dicts(
            "", players, lowBound=0, upBound=1, cat='Integer')

        problem = LpProblem("UFC_Odds_Maximizer", LpMaximize)

        problem += lpSum([scores[i] * player_vars[i] for i in player_vars])
        problem += lpSum([salaries[i] * player_vars[i]
                          for i in player_vars]) <= 100
        problem += lpSum([player_vars[i]
                          for i in player_vars]) == self.playersPerLineup

        start_time = time.monotonic()

        manySolutions = []
        for i in range(0, self.numLineupsToGenerate):
            problem.solve()
            selected_vars = []
            for p in problem.variables():
                if p.varValue and p.varValue > 0:
                    selected_vars.append(p.name[1:].replace('_', " "))
            manySolutions.append(selected_vars)

            # Add a new constraint that the sum of all of the variables should
            # not total up to what I'm looking for (effectively making unique solutions)
            problem += lpSum([player_vars[p]
                              for p in selected_vars]) <= self.playersPerLineup - 1

        print('Generation time in seconds: ', time.monotonic() - start_time)
        return manySolutions