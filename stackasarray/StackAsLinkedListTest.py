__author__ = 'advoc'

import unittest
import StackAsLinkedList
import time
import random

class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = StackAsLinkedList()
        for x in range(0, 100):
            val = random.randint(1,100)
            if x > 50:
                print("popped off: " + str(stack.pop()))
            else:
                stack.push(val)
                print("pushed: " + str(val))
            stack.print_self()
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()