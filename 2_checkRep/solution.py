from queues import Queue, Queue_broken

def test_queue():
    q = Queue(1)
    q.enqueue(1)
    q.checkRep()
    q.dequeue()
    q.checkRep()
    q.enqueue(2)
    q.checkRep()
    q.enqueue(3)
    q.checkRep()
    q.dequeue()

def test_broken_queue():
    q = Queue_broken(1)
    q.enqueue(1)
    q.checkRep()
    q.dequeue()
    q.checkRep()
    q.enqueue(2)
    q.checkRep()
    q.enqueue(3)
    q.checkRep()
    q.dequeue()

test_queue()
test_broken_queue()