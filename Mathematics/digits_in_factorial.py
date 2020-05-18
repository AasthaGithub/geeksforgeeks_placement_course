'''
Given an integer N. The task is to find the number of digits
that appear in its factorial, where factorial is defined as,
factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.
'''

dp=[0]*10000
dp[0]=1
first_done=0   #flag to check whether dp is already calculated
def calc_dp():
    global first_done,dp
    if not first_done:
        for i in range(1,10000):
            
            dp[i]=i*dp[i-1]   #calc factorial
        first_done=1    

def digitsInFactorial(N):
    global dp
    calc_dp()
    return len(str(dp[N]))
