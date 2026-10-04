class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        import itertools
        for cs, ct in itertools.zip_longest(s, t):
            dictS[cs] = dictS.get(cs, 0) + 1
            dictT[ct] = dictT.get(ct, 0) + 1
        return dictS == dictT