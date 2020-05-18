'''
Smallest divisible number
Given a number n the task is to complete the function which returns an integer denoting the smallest number evenly divisible by each number from 1 to n.

Input:
The first line of input contains an integer T denoting the no of test cases then T test cases follow. Each line contains an integer N.

Output:
For each test case output will be in new line denoting the smallest number evenly divisible by each number from 1 to n.

Constraints:
1<=T<=50
1<=n<=25

Example(To be used only for expected output):
Input:
2
3 
6
Output:
6
60
'''

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 


dp=[0]*25
dp[0]=1
first_done=0  #a flag to check if dp is already calculated

def calc_dp():
    global first_done,dp
    if not first_done:
    
        for i in range(2,25+1):           
            dp[i-1]=i*dp[i-2]//gcd(dp[i-2],i)   #calc lcm
        first_done=1       

'''
Approach:
 recursively finding lcm of two no.s and next number in array
'''


def getSmallestDivNum(n):
    calc_dp()
    global dp
    return dp[n-1]
