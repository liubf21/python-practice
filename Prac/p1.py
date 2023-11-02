import datetime

tot_time = 0

for t in range(0, 10):
    st = datetime.datetime.now()
    sum = 0
    for i in range(0, 10000000):
        sum += i

    ed = datetime.datetime.now()
    inv = ed - st
    tot_time += inv.microseconds / (10 ** 6)

print(tot_time / 10) 
# 0.827902s