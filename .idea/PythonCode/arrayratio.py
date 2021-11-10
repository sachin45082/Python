#!/bin/python3

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    s1,s2,s3 = 0,0,0

    for i in arr:
        if i > 0:
            s1+=1
        elif i < 0:
            s2+=1
        else:
            s3+=1

    print(round(s1/l,6))
    print(round(s2/l,6))
    print(round(s3/l,6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
