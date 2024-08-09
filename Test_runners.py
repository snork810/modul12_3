from runner_and_tournament import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    def setUp(self):
        self.Vasya = Runner(name='Вася')
        self.Andrey = Runner(name="Андрей")
    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        for i in range (10):
            self.Vasya.walk()
        self.assertEqual(self.Vasya.distance, 50)
    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        for i in range (10):
            self.Andrey.run()
        self.assertEqual(self.Andrey.distance, 100)
    @unittest.skipIf(is_frozen, '')
    def test_competition(self):
        for _ in range(10):
            self.Andrey.run()
        for _ in range(10):
            self.Vasya.walk()
        self.assertNotEqual(self.Andrey.distance, self.Vasya.distance)



if __name__ == '__main__':
    unittest.main()