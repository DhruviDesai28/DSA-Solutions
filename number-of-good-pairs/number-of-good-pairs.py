class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        d ={};c=0
        for i in a:
            if i in d:
                c+=d[i]
                d[i]+=1
            else:
                d[i] = 1
        return c
                
        