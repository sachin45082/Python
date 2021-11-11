# The below script is will print the unique numbers in the provided list of numbers with the number of times it occured in the list.

def listuniquecnt(lst):
    lst.sort()
    n = -100000000
    out = []
    src = []
    cnt = 1
    for i in lst:
        if i == n:
            cnt+=1
            out[len(out)-1] = cnt
        else:
            cnt = 1
            out.append(1)
            src.append(int(i))
        n = i
    return src,out

if __name__ == '__main__':
    lst = input('Please enter the number separated by comma : ').split(sep = ',')
    #print()
    print(listuniquecnt(lst))