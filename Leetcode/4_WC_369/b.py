class Solution:
    def minSum(self, a: List[int], b: List[int]) -> int:
        oa, ob, sa, sb = a.count(0), b.count(0), sum(a), sum(b)
        ans= -1
        
        if oa==ob==0:
            if sa!=sb:
                return -1
            return sa
        
        if oa and ob:
            if sa==sb:
                ans = sa+max(oa,ob)
            elif sa>sb:
                ans = max(sa+oa, sb+ob)
            elif sa<sb:
                ans = max(sa+oa, sb+ob)
            return ans
        if oa==0:
            if sa<sb+ob:
                return -1
            else:
                return sa
        if ob==0:
            if sb<sa+oa:
                return -1
            else:
                return sb