import runner_and_tournament as rat
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = rat.Runner('Усейн', 10)
        self.runer_2 = rat.Runner('Андрей', 9)
        self.runer_3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        resr={}
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                resr[key] =value.name
            print(resr)
            cls.assertTrue(resr[list(resr.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')

    def test_1(self):
        turn_1 = rat.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        self.all_results['test_turn1'] = result

    def test_2(self):
        turn_2 = rat.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.all_results['test_turn2'] = result

    def test_3(self):
        turn_3 = rat.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.all_results['test_turn3'] = result


    if __name__ == '__main__':
        unittest.main()