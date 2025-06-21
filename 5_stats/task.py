# Insert a bug of your choosing into the stats function.

# the testing should achieve full statement coverage of
# the stats function without triggering the bug
# you've inserted into the stats function.

def stats(lst):
    min_val = None
    max_val = None
    freq = {}

    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[len(lst_sorted) // 2]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for num, count in freq.items():
        if count == mode_times:
            mode.append(num)

    print("list =", lst)
    print("min =", min_val)
    print("max =", max_val)
    print("median =", median)
    print("mode =", mode)


import unittest

class TestStats(unittest.TestCase):
    def test(self):
        pass