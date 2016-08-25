class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        minStart, maxLen = 0, 1
        sLen = len(s)
        i = 0
        while i < sLen:
            if sLen - i < maxLen // 2:
                break
            j, k = i, i
            while k < sLen - 1 and s[k + 1] == s[k]:
                k += 1
            i = k + 1
            while k < sLen - 1 and j > 0 and s[k + 1] == s[j - 1]:
                k += 1
                j -= 1
            newLen = k - j + 1
            if newLen > maxLen:
                minStart = j
                maxLen = newLen
        return s[minStart: minStart + maxLen]

solution = Solution()
print(solution.longestPalindrome("ccdcce"))