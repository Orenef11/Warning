import traceback, inspect
import sys


def g():

    frame = inspect.currentframe()
    print('g()')

class Foo():
    def __int__(self):
        pass

    @staticmethod
    def foo():
        frame = inspect.currentframe()
        print('full path')

