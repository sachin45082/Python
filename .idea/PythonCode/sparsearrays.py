
def matchingStrings(strings, queries):
    lst = []
    n = 0
    for q in queries:
        cnt = 0
        # print(q)
        for s in strings:
            # print(s)
            if q == s:
                # print(q,s)
                cnt+=1

        lst.append(cnt)
        n+=1
        # print(lst,n)
    return lst

if __name__ == '__main__':
    strings = input('Please enter a Master list of strings : ').split(sep = ',')
    queries = input('Please enter a lookup list of strings : ').split(sep = ',')
    # print(strings, queries)
    rtrn = matchingStrings(strings,queries)
    print(rtrn)

