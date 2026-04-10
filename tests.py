from classes import TestCase, TestCaseTest, TestResult, TestSuite, TestSuiteTest, TestLoader, TestLoaderTest, TestRunner
    
class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')
    
    def test_c(self):
        print('test_c')
        

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)