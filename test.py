import pr as tested_progr
import unittest
import sys



class TestArr(unittest.TestCase):

    def test_basic(self):
        self.cases = ("2000.12.11","2000.12.14","2000.12.17")

        self.results = ("Week is even", "Week is even", "Week is even")

        for a, r in zip(cases, results):
            with self.subTest(case=a):
                b_r = tested_progr.main(a)
                self.assertTrue((b_r==r),msg="test_basic: a = " + str(a) + ", b_r = " + str(b) + ", r = " + str(r))





def sort_test_suite():
    suite = unittest.TestSuite()

    suite.addTest(TestArr('test_basic'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    test_suite = sort_test_suite()
    runner.run(test_suite)
