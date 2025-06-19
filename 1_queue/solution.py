from queue import Queue

def test1():
    q = Queue(3)
    res = q.empty()
    if not res:
        print("test1 NOT OK")
        return
    res = q.enqueue(10)
    if not res:
        print("test1 NOT OK")
        return
    res = q.enqueue(11)
    if not res:
        print("test1 NOT OK")
        return
    x = q.dequeue()
    if x != 10:
        print("test1 NOT OK")
        return
    x = q.dequeue()
    if x != 11:
        print("test1 NOT OK")
        return
    res = q.empty()
    if not res:
        print("test1 NOT OK")
        return
    print("test1 OK")

def test2():
    q = Queue(2)
    res = q.empty()
    if not res:
        print("test2 NOT OK")
        return
    res = q.enqueue(1)
    if res is False:
        print("test2 NOT OK")
        return
    res = q.enqueue(2)
    if res is False:
        print("test2 NOT OK")
        return
    res = q.enqueue(3)
    if q.tail != 0:
        print("test2 NOT OK")
        return

    print("test2 OK")


def test3():
    q = Queue(1)
    res = q.empty()
    if res is False:
        print("test3 NOT OK")
        return
    x = q.dequeue()
    if x is not None:
        print("test3 NOT OK")
        return
    res = q.enqueue(1)
    if res is False:
        print("test3 NOT OK")
        return
    x = q.dequeue()
    if x != 1 or q.head != 0:
        print("test3 NOT OK")
        return

    print("test3 OK")


test1()
test2()
test3()
