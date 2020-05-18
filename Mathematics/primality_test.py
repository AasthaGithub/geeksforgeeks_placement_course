'''
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
'''

mod=1000  #max no to check

#cumulative/prefix array
primeBool=[0]*(mod+1)

#special cases
primeBool[2]=1
#primeBool[1]=primeBool[0]=0

first_done=0

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

def isPrime(N):
    calc_dp()
    if primeBool[N]:
        return True
    return False
