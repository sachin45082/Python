
def minmaxsum(a,b):
    s = 0
    l = len(a)
    i = 0
    while i < int(b):
        s+=int(a[i])
        i+=1
    return s

if __name__ == '__main__':
    inpt = input('Please enter 5 positive integers separated by comma : ')
    inpt2 = input('Please enter the number of element for min max sum : ')
    lst = inpt.split(',')
    lst.sort()
    print(lst)
    mini = minmaxsum(lst,inpt2)
    lst.sort(reverse = True)
    print(lst)
    maxm = minmaxsum(lst,inpt2)
    print(mini,maxm)