import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_tes=Runner('Proba')
        for i in range(0,10):
            walk_tes.walk()
        self.assertEqual(walk_tes.distance,50)

    def test_run(self):
        ran_tes=Runner('Proba')
        for i in range(0,10):
            ran_tes.run()
        self.assertEqual(ran_tes.distance,100)

    def test_challenge(self):
        walk_tes=Runner('Proba')
        ran_tes = Runner('Proba')
        for i in range(0,10):
            walk_tes.walk()
            ran_tes.run()
        self.assertNotEqual(walk_tes.distance,ran_tes.distance)


if __name__ == "__main__":
    unittest.main()
