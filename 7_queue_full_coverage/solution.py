import unittest
from queue import Queue

class TestCase(unittest.TestCase):
    def test(self):
        q = Queue(2)
        assert q
        q.checkRep()

        empty = q.empty()
        assert empty is True, "empty() should return True"

        full = q.full()
        assert full is False, "full() should return False"

        result = q.dequeue()
        assert result is None
        q.checkRep()

        result = q.enqueue(1)
        assert result is True, "enqueue() should return True"
        q.checkRep()

        result = q.enqueue(2)
        assert result is True, "enqueue() should return True"
        q.checkRep()

        empty = q.empty()
        assert empty is False, "empty() should return False"
        q.checkRep()

        full = q.full()
        assert full is True, "full() should return True"

        result = q.enqueue(3)
        assert result is False, "enqueue() should return False"
        q.checkRep()

        result = q.dequeue()
        assert result == 1
        q.checkRep()

        result = q.dequeue()
        assert result == 2
        q.checkRep()
