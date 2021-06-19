import time
import random
import copy
import json


class GeneticGenerator:
    def __init__(self, fighterData, playersPerLineup, salaryCap, duration=20):
        self.fighterData = fighterData
        self.playersPerLineup = playersPerLineup
        self.salaryCap = salaryCap
        self.duration = duration

        self.all_lineups = []
        self.top_150 = []
        self.lineupsGenerated = 0

    def __add_lineup_to_top_150(self, lineup):
        # Sort the lineup
        for i in range(1, len(lineup)):
            key = lineup[i]
            j = i-1
            while j >= 0 and key['score'] > lineup[j]['score']:
                lineup[j+1] = lineup[j]
                j -= 1
            lineup[j+1] = key
        # Check if top 150 contains this already
        if not lineup in self.top_150:
            self.top_150.append(lineup)

    # Get the total score of a lineup
    def __getLineupScore(self, lineup):
        lineupScore = 0
        for player in lineup:
            lineupScore += player['score']
        return lineupScore

    # Insertion sort a list of lineups based on total lineup score
    def __sortLineups(self, unsorted):
        for i in range(1, len(unsorted)):
            key = unsorted[i]
            j = i-1
            currentLineupScore = self.__getLineupScore(unsorted[i])
            while j >= 0 and currentLineupScore < self.__getLineupScore(unsorted[j]):
                unsorted[j+1] = unsorted[j]
                j -= 1
            unsorted[j+1] = key
        return unsorted

    def __get_lineups(self, fighters):
        # Generate 10 new lineups
        new_lineups = [self.__generate_lineup(fighters) for _ in range(10)]

        # Sort the lineups by their predicted score
        new_lineups = self.__sortLineups(new_lineups)

        # Add the newly created lineups to the self.top_150 (they will be sorted and bottom ones removed later)
        for j in new_lineups:
            self.__add_lineup_to_top_150(j)

        # Mate the top 3 lineups together
        offspring_1 = self.__mate_lineups(new_lineups[0], new_lineups[1])
        offspring_2 = self.__mate_lineups(new_lineups[0], new_lineups[2])
        offspring_3 = self.__mate_lineups(new_lineups[1], new_lineups[2])

        # Mate the offspring with a randomly selected lineup from the self.top_150 and add to self.top_150
        # Adding this step makes the algorithm more greedy, and produces higher projections, but can be skipped
        self.__add_lineup_to_top_150(self.__mate_lineups(
            offspring_1, self.top_150[random.randint(0, len(self.top_150) - 1)]))
        self.__add_lineup_to_top_150(self.__mate_lineups(
            offspring_2, self.top_150[random.randint(0, len(self.top_150) - 1)]))
        self.__add_lineup_to_top_150(self.__mate_lineups(
            offspring_3, self.top_150[random.randint(0, len(self.top_150) - 1)]))

        # Add the original offspring to the self.top_150
        self.__add_lineup_to_top_150(offspring_1)
        self.__add_lineup_to_top_150(offspring_2)
        self.__add_lineup_to_top_150(offspring_3)

    def __mate_lineups(self, lineup1, lineup2):
        # Create list of all fighters contained between the two lists
        fighters = lineup1 + lineup2

        while True:
            # Create the new lineup by selecting players from each position list
            available_fighters = copy.deepcopy(fighters)
            selected_fighters = []
            while len(selected_fighters) < self.playersPerLineup:
                i = random.randint(0, len(available_fighters) - 1)
                selected_fighters.append(available_fighters[i])
                del available_fighters[i]
            lineup = selected_fighters
            # Check if the lineup is valid (i.e. it satisfies some basic constraints)
            lineup = self.__check_valid(lineup)

            # If lineup is valid, return it, otherwise keep trying
            if lineup:
                return lineup

    def __check_valid(self, lineup):
        # Remove duplicate players from lineup and count how many players
        seen_names = set()
        new_list = []
        for i in lineup:
            if i['name'] not in seen_names:
                new_list.append(i)
                seen_names.add(i['name'])
        lineup = new_list

        # calculate the total salary used for the lineup
        salary = sum(player['salary'] for player in lineup)

        # Check if lineup contains fighters in same fight
        bothFighters = False
        seenOpponents = []
        for i in lineup:
            if i['name'] in seenOpponents:
                bothFighters = True
                break
            seenOpponents.append(i['opponentName'])

        # check the salary cap and number of players in lineup
        if salary <= self.salaryCap and len(lineup) == self.playersPerLineup and not bothFighters:
            self.lineupsGenerated += 1
            return lineup
        return False

    def __generate_lineup(self, fighters):
        while True:
            # add the correct number of each position to a lineup
            lineup = []
            for _ in range(0, self.playersPerLineup):
                lineup.append(fighters[random.randint(0, len(fighters) - 1)])

            # Check if the lineup is valid (i.e. it satisfies some basic constraints)
            lineup = self.__check_valid(lineup)

            if lineup:
                return lineup

    # Run the genetic algorithm
    def run(self):
        runtime = time.time() + self.duration
        while time.time() < runtime:
            self.__get_lineups(self.fighterData)
            # Sort top 150
            sorted_top_150 = self.__sortLineups(self.top_150)
            sorted_top_150.reverse()
            self.all_lineups = sorted_top_150
            finalLineups = sorted_top_150[:150]
            self.top_150 = finalLineups
        print('Total lineups generated: ' + str(self.lineupsGenerated))
        return self.top_150
