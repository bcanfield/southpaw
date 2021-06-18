from southpaw.generators.linear import LinearGenerator
from southpaw.tests import test_data_file_path

def test_linear():
    salaryCap = 100
    scoreColumnName = 'score'
    playersPerLineup = 6
    numLineupsToGenerate = 10
    linearGenerator = LinearGenerator(
        test_data_file_path, salaryCap, playersPerLineup, scoreColumnName, numLineupsToGenerate)
    generatedLineups = linearGenerator.run()
    assert len(generatedLineups) == 10
