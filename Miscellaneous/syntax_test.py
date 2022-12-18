#file name should start with test_ or _test
#pytest method name should start with test
#any code should be wrapped in method
#can not have multple methods with the same name

def test_syntax():
    print("Hello")
# -k will work as a regular expression -k merthod name will run the test
# -s prints the logs
# -v for more info (metadata)
# directory>py.test filename -v -s
# -m test marked python file
