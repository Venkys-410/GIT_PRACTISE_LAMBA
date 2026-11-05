from collections import deque

def window(iterable, size):
    result = deque(maxlen=size)
    for item in iterable:
        result.append(item)
        if len(result) == size:
            yield result

for r in window([1,2,3,4,5],3):
    # print(list(r))
    print(r)