# Collections
# Basic Data structures in Python: List, Set, Tuple, Dictionary

# Advance collections: ---generally these are not used in automation
    # deque - Queue
    # defaultDict
    # Counter
    # OrderedDict -----used in automation
    # ChainMap
    # nametuple

#deque - double ended queue
# FIFO - First in First out

from collections import deque
#create a deque
d = deque()
d1 = deque([1,2,3])
print(d1)
d.append(5)
print(d)

#Add an element to the left end
d1.appendleft(0)
print(d1)

#Extend the deque from the left with an iterable
d1.extend([4])
print(d1)

d.extend([2, 9])
print(d)

#append - add one element
# extend - add a list of multiple elements

print(d.pop())
print(d.popleft())
print(d)


