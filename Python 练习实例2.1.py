#!/usr/bin/python3
i=int(input("请输入你的利润额:"))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.01]
r=0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
