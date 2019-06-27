import time
t1 = time.time()
a = b = c = 0
for m in range(10000000):
    # 判断输赢
    if m %3 == 0:
        a  += 1
    elif m %3 == 1:
        b += 1
    else:
        c += 1
t2 = time.time()
print(t2-t1)