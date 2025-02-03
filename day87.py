T=int(input('Enter no of testcases : '))
for _ in range(T):
    N=int(input('Enter no of stones : '))
    st=list(map(int,input().split()))
    i,j=0,0
    stones=0
    while j<N:
        if st[j]>=st[i]:
            j+=1
        else:
            stones+=(j-i+1)*st[i]-st[j]
            i=j
    stones+=(N-i)*st[i]-st[N-1]
    if stones<0:
        print(0)
    else:
        print(stones)
