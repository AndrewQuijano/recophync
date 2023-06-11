import os
import unittest
import glob
import csv
from RecoPhyNC import open_network, contract
from RecoPhyNC import computeLevel


def read_test_answers() -> dict:
    answer_key = dict()
    with open('answers.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            file_name = row['file']
            del row['file']
            answer_key[file_name] = row
    return answer_key


class TestRecoPhyNC(unittest.TestCase):
    test_directory = "data"
    folder = os.getcwd()
    file_filter = "*"

    @classmethod
    def setUpClass(cls):
        cls.answer = read_test_answers()

    def test_level_k(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

            # Compute level and compare
            level = computeLevel(network)
            self.assertTrue(level == self.answer[data_file]['level'])

    def test_tree_child(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

    def test_nearly_tree_child(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

    def test_genetically_stable(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

    def test_reticulation_visible(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

    def test_tree_sibling(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

    def test_compressed(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)

    def test_nearly_stable(self):
        for data_file in glob.glob(os.path.join(self.folder, self.test_directory, self.file_filter)):
            # network initialization and preprocessing
            network = open_network(data_file)
            contract(network)


if __name__ == '__main__':
    unittest.main()
