from southpaw.generators.genetic import GeneticGenerator
import json


def test_genetic():
    jsonDataFilePath = 'southpaw/tests/testData/testFighterData.json'
    f = open(jsonDataFilePath,)
    fighterData = json.load(f)
    salaryCap = 100
    playersPerLineup = 6
    numLineupsToGenerate = 10
    geneticGenerator = GeneticGenerator(fighterData, playersPerLineup, salaryCap, 20)
    geneticGenerator.run()
    generatedLineups = geneticGenerator.run()
    assert len(generatedLineups) == 150
