import unittest


class MyTestCase(unittest.TestCase):
    def factorial(num):
        assert type(num)==type(1)
        assert num>=0
        self.assertGreater(num,0,'Yes,greater')
        if (num==0):
            return 1
        else:
            return num*factorial(num-1)



if __name__ == '__main__':
    unittest.main()
