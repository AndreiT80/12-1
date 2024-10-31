# Домашнее задание по теме "Простые Юнит-Тесты"  tests_12_1.py

import unittest
from Runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """ test_walk - метод, в котором создаётся объект класса Runner
        с произвольным именем. Далее вызовите метод walk у этого объекта
         10 раз. После чего методом assertEqual сравните distance этого
         объекта со значением 50.
        """
        rn = Runner("Bil")
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        """ test_run - метод, в котором создаётся объект класса Runner с
        произвольным именем. Далее вызовите метод run у этого объекта 10 раз.
         После чего методом assertEqual сравните distance этого объекта со
         значением 100.
        """
        rn1 = Runner("Not")
        for i in range(10):
            rn1.run()
        self.assertEqual(rn1.distance, 100)

    def test_challenge(self):
        """ test_challenge - метод в котором создаются 2 объекта класса Runner
         с произвольными именами. Далее 10 раз у объектов вызываются методы
         run и walk соответственно. Т.к. дистанции должны быть разными,
         используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        """
        rn2 = Runner("Bil")
        rn3 = Runner("Not")
        for i in range(10):
            rn2.walk()
            rn3.run()
        self.assertNotEqual(rn2.distance, rn3.distance)


if __name__ == "__main__":
    unittest.main()

    ''' unittest запускается из терминала командной стракой

        python -m unittest -v test_Runner.py
     '''
