from southpaw.generators.genetic import GeneticGenerator


def test_genetic():
    jsonDataFilePath = 'southpaw/tests/testData/testFighterData.json'
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    geneticGenerator = GeneticGenerator(jsonDataFilePath, playersPerLineup, salaryCap, 20)
    geneticGenerator.run()
    generatedLineups = geneticGenerator.run()
    assert len(generatedLineups) == 150
