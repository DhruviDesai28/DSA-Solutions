class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d={};
        for i in words[0]:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in range(1, len(words)):
            t = {}
            for j in words[i]:
                if j not in t:
                    t[j]=1  
                else:
                    t[j]+=1
            for i in d:
                if i in t:
                    d[i] = min(d[i],t[i])
                else:
                    d[i]=0
        x = []
        for i in d:
            while d[i]!=0:
                x.append(i)
                d[i]-=1
        return(x)
            
            
                
        