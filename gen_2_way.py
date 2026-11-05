def running_average():
    total, n, avg = 0, 0, None
    while True:
        x = yield avg          # receive a value here
        total += x
        n += 1
        avg = total / n
 
a = running_average()
print(next(a))                     # 'prime' it: run to the first yield
print(a.send(10), a.send(20), a.send(30))   # 10.0 15.0 20.0
