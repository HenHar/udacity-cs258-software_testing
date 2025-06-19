# THE CORRECT SPECIFICATION:
#
# The Queue class provides a fixed-size FIFO queue of integers
#
# - The constructor takes a single parameter: an integer > 0 that
#   is the maximum number of elements the queue can hold.
#
# - is_empty() returns True if and only if the queue currently
#   holds no elements, and False otherwise.
#
# - is_full() returns True if and only if the queue cannot hold
#   any more elements, and False otherwise.
#
# - enqueue(i) attempts to put the integer i into the queue; it returns
#   True if successful and False if the queue is full.
#
# - dequeue() removes an integer from the queue and returns it,
#   or else returns None if the queue is empty.
#
# Example:
#   q = Queue(1)
#   is_empty = q.empty()
#   succeeded = q.enqueue(10)
#   is_full = q.full()
#   value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which should be 10
#
# Homework:
#
# There are five buggy implementations of the Queue in queue_test. The correct
# queue specification is above. Your homework is to write assertions that
# cause all five buggy implementations to fail.

import sys
from buggy_queues import *


def correct_test():
    Queue = Queue5

    # Queue1 silently holds only 2 byte unsigned integers, than wraps around
    q = Queue(2)
    succeeded = q.enqueue(100000)
    assert succeeded
    value = q.dequeue()
    assert value == 100000

    # Queue2 silently fails to hold more than 15 elements
    q = Queue(30)
    for i in range(20):
        succeeded = q.enqueue(i)
        assert succeeded

    # Queue3 implements empty() by checking if dequeue() succeeds.
    # This changes the state of the queue unintentionally.
    q = Queue(2)
    succeeded = q.enqueue(10)
    assert succeeded
    assert not q.empty()
    value = q.dequeue()
    assert value == 10

    # Queue4 dequeue() of an empty queue returns False instead of None
    q = Queue(2)
    value = q.dequeue()
    assert value == None

    # Queue5 holds one less item than intended
    q = Queue(2)
    for i in range(2):
        succeeded = q.enqueue(i)
        assert succeeded

correct_test()