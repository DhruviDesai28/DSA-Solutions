#User function Template for python3

class Solution:
    def countSquares(self, x):
        l,r = 1, x
        ans = 0
        while l<=r:
            m = l+(r-l)//2
            msq = m*m
            if msq>=x:
                r = m-1
            else:
                ans = m
                l = m+1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends