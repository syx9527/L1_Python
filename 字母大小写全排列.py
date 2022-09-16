class Solution(object):
    def letterCasePermutation(self, S):
        res = [""]
        for c in S:
            next_res = []
            for tmp in res:
                next_res.append(tmp + c)
                if not c.isdigit():
                    c = c.upper() if c.islower() else c.lower()
                    next_res.append(tmp + c)
            res = next_res
        res.sort()
        return res


if __name__ == '__main__':
    S = input()
    s = Solution()
    res = s.letterCasePermutation(S=S)

    print(res)
