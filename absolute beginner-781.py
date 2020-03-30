n=int(input())
if(n==0):
    print("NULL")
else:
    l=[i for i in range(9,(9*n)+1,9)]
    print("".join(l))
