#Collections module. 
# - Collections.deque class supports push and pop on both ends so, can also be used as Stack.
# - Implemented using DLL.
# - It can also be instanciated with max_size and if the size exceeds it will delete the front elements so, be carefull

from collections import deque

q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.popleft()
print(q)
q.clear()
print(q)

#Queue module
# - This module implements multi producer and multi consumer queues. Useful for threaded programming.
# - It has Three implementations:
# - FIFO queue
# - LIFO queue - Stack
# - Priority queue - The entries are kept sorted and lowest value entry is retreived first.

import queue as q

customeQueue = q.Queue(maxsize=3)
print(customeQueue.qsize())
customeQueue.put(1)
customeQueue.put(2)
customeQueue.put(3)
print(customeQueue.full())
print(customeQueue.get())
print(customeQueue.qsize())


#Multiprocessing module
# - Allowes queue items to be processed by multiple workers parallely

from multiprocessing import Queue

customeQueue = Queue(maxsize=3)
customeQueue.put(1)
print(customeQueue.get())
