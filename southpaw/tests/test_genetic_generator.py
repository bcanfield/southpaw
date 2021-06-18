from southpaw.generators.genetic import GeneticGenerator
from southpaw.tests import test_data_file_path


def test_genetic():
    salaryCap = 100
    playersPerLineup = 6
    geneticGenerator = GeneticGenerator(
        test_data_file_path, playersPerLineup, salaryCap, 20)
    geneticGenerator.run()
    generatedLineups = geneticGenerator.run()
    assert len(generatedLineups) == 150
