class Solution:
    def maxArea(self, a: List[int]) -> int:
        l,r = 0,len(a)-1; d = 0
        while l<r:
            if a[l]<=a[r]:
                c = a[l]*(r-l)
                l+=1
            else:
                c = a[r]*(r-l)
                r-=1
            if c>d: d = c
        return (d)
