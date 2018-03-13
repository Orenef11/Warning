''' Demo script experimenting with various features of the
inspect module
'''
# To be run with Python3.3


from inspect_test import MyClass
from inspect_test import myfunc
from inspect_test import mygen

import inspect
from inspect import signature

# if __name__ == '__main__':
#
#     # demo of inspect.getsource()
#     obj = MyClass()
#
#     # Get the source file where this class
#     if inspect.isclass(MyClass):
#         print(inspect.getsource(MyClass))
#
#     # demo of inspect.getmembers()
#
#     # Get the members
#     print('Object Members:: \n')
#     allMember = inspect.getmembers(obj)
#     for member in allMember:
#         print(member)
#
#     print('\n\nRandom Expirements \n')
#
#     # experiments with builtins
#     functions = [obj.fun1, open, dir, myfunc]
#     for func in functions:
#         if inspect.isbuiltin(func):
#             print('{0:s} is built in'.format(func.__name__))
#         else:
#             print('{0:s} is not built in'.format(func.__name__))
#
#     print('\n')
#     # experiments with signatures
#     # Introduced in Python 3.3
#     functions = [obj.fun1, inspect.isclass]
#     for func in functions:
#         sig = signature(func)
#         print('Parameters: {0:s}:: {1:s}'.format(func.__name__, str(sig)))
#
#     print('\n')
#
#     # experiments with frames
#     myfunc()
#
#     # generator experiments
#     generator = mygen()
#
#     # get the current state
#     print(inspect.getgeneratorstate(generator))
#
#     count = 0
#     for fib in generator:
#         # get the current state
#         print(inspect.getgeneratorstate(generator))
#
#         # print the number yielded
#         print(fib)
#         if count >= 10:
#             break
#         count = count + 1
#
#     print(inspect.getgeneratorstate(generator))
#
#
#     print (inspect.isbuiltin.__module__)
#     print(inspect.isbuiltin.__name__)
#     print(inspect.isbuiltin.__class__)


def getTrace():
    trace = inspect.stack()
    tracecaller = []

    for frame in trace:
        currentFrame = 'Module :{fileName} - function name : {function}'.format(fileName=inspect.getmodulename(frame.filename),function=frame.function)
        tracecaller.append(currentFrame)
    return '{currentFunction} <- {previousFunction}'.format(currentFunction=tracecaller[1],previousFunction=tracecaller[2])

def b():
    result = False
    print(getTrace())
    print("b")

def a():
    b()
    sta = inspect.stack()
    print("a")


class foo:
    def __int__(self):
        pass

    @staticmethod
    def c():
        a()
        print('func c')

foo.c()
loca = locals()
print (locals())