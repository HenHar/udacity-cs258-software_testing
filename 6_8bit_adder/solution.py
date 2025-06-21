import unittest
from adder import add8


class TestAdder(unittest.TestCase):
    def glue(self, a0, a1, a2, a3, a4, a5, a6, a7, c):
        t = 0
        if a0:
            t += 1
        if a1:
            t += 2
        if a2:
            t += 4
        if a3:
            t += 8
        if a4:
            t += 16
        if a5:
            t += 32
        if a6:
            t += 64
        if a7:
            t += 128
        if c:
            t += 256
        return t

    def split(self, n):
        return n & 0x1, n & 0x2, n & 0x4, n & 0x8, n & 0x10, n & 0x20, n & 0x40, n & 0x80

    def myadd(self, a, b):
        a0, a1, a2, a3, a4, a5, a6, a7 = self.split(a)
        b0, b1, b2, b3, b4, b5, b6, b7 = self.split(b)
        s0, s1, s2, s3, s4, s5, s6, s7, c = add8(a0, a1, a2, a3, a4, a5, a6, a7, b0, b1, b2, b3, b4, b5, b6, b7, False)
        return self.glue(s0, s1, s2, s3, s4, s5, s6, s7, c)

    def testExhaustive(self):
        for i in range(256):
            for j in range(256):
                res = self.myadd(i,j)
                #print(str(i) + " + " + str(j) + " = " + str(res))
                assert  res == (i+j)