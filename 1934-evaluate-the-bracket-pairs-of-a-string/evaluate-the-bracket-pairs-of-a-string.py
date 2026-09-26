class Solution:
    def get_end(self, s, start):
        l = len(s)
        pos = start
        end = start
        
        found = False
        while pos < l:
            if s[pos] == ")":
                end = pos
                found = True
                break
            pos = pos + 1
        
        if not found:
            return -1
        
        return end

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i = 0
        map = dict(knowledge)
        res = ""
        while i < len(s):
            if s[i] == "(":
                # extract the key from the parenthesis
                end = self.get_end(s, i)

                # if there is no closing ")"
                if end == -1:
                    return res + s[i:len(s)]
                
                # actual key
                substr = s[i+1:end]
                print(substr)

                # find the value
                val = "?"
                if substr in map: # store key:value pairs in own map for faster lookup
                    val = map[substr]
                
                # add the found value to the result
                res += val
                i = end+1
            else: # else just add current char to the result
                res += s[i]
                i = i+1

        return res