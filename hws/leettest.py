class solution:
    def myAtoi(self, s: str) -> int:
            s = s.strip()
            if s[0] == "-":
                flag = -1
                s = s[1:]
            if s[0] == "+":
                flag = 1
                s = s[1:]
            flag = 1
            res = "0"
            for i in s:
                if i.isdigit() and i != "0":
                    res += i
                elif i == "0":
                    continue
                else:
                    break
            res *= flag
            res = int(res)
            return res

ins = solution()

print(ins.myAtoi("  -42"))