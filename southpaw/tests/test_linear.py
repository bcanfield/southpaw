from southpaw.generators.linear import LinearGenerator

def test_linear():
    jsonDataFilePath = 'southpaw/tests/testFighterData.json'
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    lg = LinearGenerator(jsonDataFilePath, salaryCap, scoreColumnName, playersPerLineup, numLineupsToGenerate)
    assert len(lg) == 10
