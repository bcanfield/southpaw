from southpaw.generators.linear import LinearGenerator
from southpaw.tests import test_data_file_path
import pandas as pd

def test_linear():
    jsonDataFilePath = 'southpaw/tests/testData/linearTestData.json'
    inputData = pd.read_json(jsonDataFilePath)
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    linearGenerator = LinearGenerator(
        inputData, salaryCap, playersPerLineup, scoreColumnName, numLineupsToGenerate)
    generatedLineups = linearGenerator.run()
    assert len(generatedLineups) == 10