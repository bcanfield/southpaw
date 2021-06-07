from southpaw.generators.linear import LinearGenerator


def test_linear():
    jsonDataFilePath = 'southpaw/tests/testFighterData.json'
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    linearGenerator = LinearGenerator(
        jsonDataFilePath, salaryCap, scoreColumnName, playersPerLineup, numLineupsToGenerate)
    generatedLineups = linearGenerator.generate()
    assert len(generatedLineups) == 10
