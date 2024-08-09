from runner_and_tournament import Runner, Tournament
import unittest
from pprint import pprint
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        print('Список участников')
        self.first_runner = Runner('Usein', 10)
        self.second_runner = Runner('Andrei', 9)
        self.third_runner = Runner('Nic', 3)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tour(self):
        t = Tournament(90, self.first_runner, self.third_runner)
        self.results = t.start()
        self.assertTrue(self.results[2], 'Nic')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tour(self):
        t = Tournament(90, self.second_runner, self.third_runner)
        self.results = t.start()
        self.assertTrue(self.results[2], 'Nic')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tour(self):
        t = Tournament(90, self.first_runner,self.second_runner,  self.third_runner)
        self.results = t.start()
        self.assertTrue(self.results[3], 'Nic')

    def tearDown(self):
        self.all_results.append(self.results)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

if __name__ == '__main__':
    unittest.main()