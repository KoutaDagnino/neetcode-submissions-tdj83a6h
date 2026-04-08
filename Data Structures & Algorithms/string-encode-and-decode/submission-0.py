class Solution:

    def encode(self, strs: List[str]) -> str:
        result="256"
        for string in strs:
            for c in string:
                ASCII_ind = str(ord(c))
                if len(ASCII_ind)==1:
                    ASCII_ind = "00"+ASCII_ind
                elif len(ASCII_ind)==2:
                    ASCII_ind = "0"+ASCII_ind
                result+=ASCII_ind
            result+="256"
        return result

    def decode(self, s: str) -> List[str]:
        ind_list = [int(s[i:i+3]) for i in range(0,len(s),3)]
        str_list = []
        for ind in ind_list:
            if ind==256:
                str_list.append("")
            else:
                str_list[-1]+=chr(ind)
        return str_list[:-1]