class Solution(object):
    def SubarraysWithKDistinct(self, A, K):
        s = collections.Counter() 
        l = r = ans = 0 
        for i,num in enumerate(A):
            s[num] += 1
            if s[num] == 1 and len(s) == K:
                while r < len(A) and A[r] in s:
                    r += 1 
                while len(s) == K:
                    ans += r-i 
                    s[A[l]] -= 1 
                    if s[A[l]] == 0: del s[A[l]] 
                    l += 1 
        return ans
        