class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(str(len(string))))+str(len(string))+string
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            ll = int(s[0])
            l = int(s[1:ll+1])
            strs.append(s[ll+1:ll+1+l])
            s = s[ll+1+l:]
        return strs