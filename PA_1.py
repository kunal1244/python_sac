T=int(input())                                         # input no. of test cases
l=[]
if T>=1 and T<=100:                                    # check if no. of test cases is between 1 and 100
    for i in range(T):                              
        N,K =input().split()
        N,K=int(N),int(K)                              # taking input and converting to integers
        if N>=1 and N<=10000:
            if K>=1 and K<=10000:                      # checking if N and K are in between 1 and 10000
                l_st=input().split()
                for elem in l_st:
                    l.append(int(elem))
                rem_shift=K%N                          # finding shift as remainder of array size
                new_l=[0 for k in range(N)]            # initialize rotated array
                for k in range(N):
                    ind=(k-rem_shift+N)%N              # finding new index for an element
                    new_l[ind]=l[k]
                for i in new_l: print (i,end=' ')      # output
            else:
                print("No. of shifts must lie between 1 and 10000")
        else:
            print("No. of elements must lie between 1 and 10000")
else:
    print("No. of test cases must be between 1 and 100!!!")
