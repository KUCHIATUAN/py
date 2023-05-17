import random
import time

ans=random.randint(1, 100)

while True:
    nn=int(input("請輸入數字:"))
    if nn==0:
        break
    elif nn>ans:
        print("TOO BIG!!!")
    elif nn<ans:
        print("TOO SMALL!!!")
    else:
        print("答對了")
        time.sleep(3)
        ans=random.randint(1, 100)
       