import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(4)
q.put(5)
q.get()
q.get()
# -------------deque 방법------------ #
from collections import deque

queue = deque([1, 2])

queue.append(4)
queue.append(5)
queue.append(3)
queue.popleft()
queue.append(8)
queue.append(6)
queue.popleft()