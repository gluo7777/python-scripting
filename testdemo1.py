import unittest

# Test Suite
# Test Cases
# Assertions

# Test some methods
class TestCase1(unittest.TestCase):

    def test_something1(self):
        self.assertEqual('William','William')
        self.assertEqual('William'.upper(),'WILLIAM')
        self.assertTrue('WILLIAM'.isupper())

    def test_something2(self):
        self.assertIn('b',['a','b','c'])
    
    def test_something_fail1(self):
        self.assertTrue(True,'test_something_fail1 failed!')

class TestCase2(unittest.TestCase):

    def test_something21(self):
        self.assertGreaterEqual(3,2)

class TestCase3(unittest.TestCase):

    def setUp(self):
        self.name = 'William'

    def test_somethingA(self):
        self.assertEquals(self.name,'William')

    def test_exception(self):
        with self.assertRaises(ValueError):
            int('A')

    def not_a_test_but_returns(self):
        return '{name} is here!'.format(name=self.name)
    
    @unittest.skipIf(True, 'skipping trivial test')
    def test_trivial(self):
        print(self.not_a_test_but_returns())

    def tearDown(self):
        self.name = None

def get_test_suite():
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    suite = unittest.TestLoader().loadTestsFromName('testdemo1')
    # suite = unittest.TestSuite()
    # suite.addTest(TestCase1())
    # suite.addTest(TestCase2())
    # suite.addTest(TestCase3())
    return suite

def main():
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.TextTestRunner(verbosity=2).run(get_test_suite())

if __name__ == '__main__':
    main()