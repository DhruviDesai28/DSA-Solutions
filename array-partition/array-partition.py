class Solution:
    def arrayPairSum(self, a: List[int]) -> int:
        a.sort()
        c = 0
        for i in range(len(a)//2):
            c+=a[2*i]
        return c
        