from southpaw.generators.linear import LinearGenerator
from southpaw.tests import test_data_file_path
import json

def test_linear():
    jsonDataFilePath = 'southpaw/tests/testData/linearTestData.json'
    with open(jsonDataFilePath, 'r') as myfile:
        data=myfile.read()
    inputData = json.loads(data)
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    linearGenerator = LinearGenerator(
        inputData, salaryCap, playersPerLineup, scoreColumnName, numLineupsToGenerate)
    generatedLineups = linearGenerator.run()
    assert len(generatedLineups) == 10