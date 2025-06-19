# TASK:
#
# This is the SplayTree code we saw earlier in the
# unit. We didn't achieve full statement coverage
# during the unit, but we will now!
# Your task is to achieve full statement coverage
# on the SplayTree class.
#
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the
#    entire code base.
#
# You can also run your code through a code coverage
# tool on your local machine if you prefer. This is
# not necessary, however.
# If you have any questions, please don't hesitate
# to ask in the forums!


import unittest
from splay import SplayTree, Node


class TestCase(unittest.TestCase):
    def setUp(self):
        self.keys = [0, 1, 2, 3, 5, 4, 5, 6, 7, 9, 8]
        self.not_present_value = -999
        self.t = SplayTree()
        for key in self.keys:
            self.t.insert(key)

    def testInsert(self):
        for key in self.keys:
            self.assertEqual(key, self.t.find(key))

        assert self.t.insert(self.keys[-1]) is None

    def testRemove(self):
        assert self.t.remove(self.not_present_value) is None

        for key in self.keys:
            self.t.remove(key)
            self.assertEqual(self.t.find(key), None)

    def testLargeInserts(self):
        t = SplayTree()
        nums = 40000
        gap = 307
        i = gap
        while i != 0:
            t.insert(i)
            i = (i + gap) % nums

    def test_isEmpty(self):
        t = SplayTree()
        t.splay(4)
        isEmpty = t.isEmpty()
        assert isEmpty is True

    def test_findMax(self):
        tree = SplayTree()
        assert tree.findMax() is None

        max_value = self.t.findMax()
        assert max_value == 9

    def test_find(self):
        tree = SplayTree()
        assert tree.find(self.not_present_value) is None

    def test_findMin(self):
        tree = SplayTree()
        assert tree.findMin() is None

        max_value = self.t.findMin()
        assert max_value == 0

    def test_Node(self):
        node = Node(3)
        assert node.equals(Node(3)) is True
        assert node.equals(Node(4)) is False

