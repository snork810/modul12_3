import unittest
import Test_runners
import Tests_tournament

run_compTS = unittest.TestSuite()
run_compTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_runners.RunnerTest))
run_compTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_compTS)