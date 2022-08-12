from Selenium_Practice.LetsCodeIt.test1 import Practice


class TestFile():
    def test(self):
        test_run = Practice()
        test_run.fun1()
        test_run.newWindow()

obj = TestFile()
obj.test()