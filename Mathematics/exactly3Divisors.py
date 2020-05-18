'''
Given a positive integer value N. The task is to find how many 
numbers less than or equal to N 
have numbers of divisors exactly equal to 3.
'''

'''
Approach :
Only squares of prime no.s have 3 divisors
'''

mod=1000
primeBool=[0]*(mod+1)

#Note that prefix arr size square of that of primeBool array
#cumulative/prefix boolean array that stores whether a number i at index i is square of prime number or not
pre=[0]*(1000000)


#handling special cases of prime numbers
primeBool[2]=1
primeBool[1]=primeBool[0]=0

#variables to keep check if primeBool array and prefix array 'pre'
#have already been calculated by calc_dp() and calc_pre() methods already
first_done=0
second_done=0


#makes index i as 1 if it's prime
#sieve of erastosthenes approach

def calc_dp():
    global first_done,primeBool,mod
    if not first_done:
        for i in range(3,mod+1,2):
        	primeBool[i]=1
        for i in range(3,mod+1,2):
        	if primeBool[i]==1:
        		for j in range(i*i,mod+1,i):
        			primeBool[j]=0
        first_done=1


#makes square of prime numbers (index i)==1
def calc_pre():
    global pre,second_done,primeBool
    if not second_done:
        for i in range(2,mod):
            if primeBool[i]:
                pre[i*i]=1
    second_done=1       


#method to interact with above methods and
#return number of integers less than N with 3 divisors

def exactly3Divisors(N):
    calc_dp()
    calc_pre()
    global primeBool,pre
    if N==1 or N==2:
        return 0
    else:
        return sum(pre[:N+1])

 #compromising space O(n) or some time in pre-check while building prefix array we could remove sum function as well  
