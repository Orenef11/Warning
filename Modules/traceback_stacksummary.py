import traceback ,inspect
import sys

import traceback_example



def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    traceback_example.g()
    Inspect=inspect
    frame = inspect.currentframe()
    print(''.join(summary.format()))


print('Calling f() directly:')
f()


frame = inspect.currentframe()
print ('hello')
traceback_example.Foo.foo()
