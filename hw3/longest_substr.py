def lengthOfLongestSubstring(s: str) -> int:
    m = set()
    res = 0
    for start in range(0, len(s)):
        local_res = 0
        for i in range(start, len(s)):
            c = s[i]
            if c in m:
                res = max(res, local_res)
                m = set()
                break
            else:
                m.add(c)
                local_res += 1

    return res


print(lengthOfLongestSubstring("pwwkew"))