import os

class Test:
    def f(self):
    	print 'Hello, World!'

class NewTest(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def say(self):
        print 'my name is ' + self.name + ' and my score is ' + self.score

if __name__ == '__main__':

    Test().f()
    test2 = NewTest('Xsb', '77')
    test2.say()
