from southpaw.generators.linear import LinearGenerator


def test_linear():
    jsonDataFilePath = 'southpaw/tests/testData/testFighterData.json'
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    linearGenerator = LinearGenerator(
        jsonDataFilePath, salaryCap, playersPerLineup, scoreColumnName, numLineupsToGenerate)
    generatedLineups = linearGenerator.run()
    assert len(generatedLineups) == 10
