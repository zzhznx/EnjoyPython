# 最长回文子序列
'''
example
input: abcfgbda
output: 5
'''

class Solution(object):
    '''
    递归
    '''
    def longestPalindrome1(self, s, i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j]:
            return self.longestPalindrome1(s, i+1, j-1) + 2
        else:
            return max(self.longestPalindrome1(s, i, j-1), self.longestPalindrome1(s, i+1, j))
    '''
    动态规划

    对任意字符串，如果头和尾相同，那么它的最长回文子序列一定是去头去尾之后的部分的最长回文子序列加上头和尾。
    如果头和尾不同，那么它的最长回文子序列是去头的部分的最长回文子序列和去尾的部分的最长回文子序列的较长的那一个

    设字符串为s，f(i,j)表示s[i..j]的最长回文子序列。
    状态转移方程如下：
    当i>j时，f(i,j)=0。

    当i=j时，f(i,j)=1。

    当i<j并且s[i]=s[j]时，f(i,j)=f(i+1,j-1)+2。

    当i<j并且s[i]≠s[j]时，f(i,j)=max( f(i,j-1), f(i+1,j) )。

    注意如果i+1=j并且s[i]=s[j]时，f(i,j)=f(i+1,j-1)+2=f(j,j-1)+2=2，这就是“当i>j时f(i,j)=0”的好处。

    由于f(i,j)依赖i+1，所以循环计算的时候，第一维必须倒过来计算，从s.length()-1到0。

    s的最长回文子序列长度为f(0, s.length()-1)


    获取长度时间复杂度O(n),空间复杂度O(n^2)
    printLCS的时间复杂度为O(n)
    '''
    def longestPalindrome2(self, s):
        count = [[0 for col in range(len(s))] for row in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            count[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    count[i][j] = count[i+1][j-1] + 2
                else:
                    count[i][j] = max(count[i][j-1], count[i+1][j])

        self.printLPS(s, count, 0, len(s)-1)
        print()

        return count[0][len(s)-1]


    def printLPS(self, s, count, i, j):
        if j < i:
            return
        if i == j:
            print(s[i], end='')
            return
        #if count[i][j] == (count[i+1][j-1] + 2):
        if s[i] == s[j]:
            print(s[i], end='')
            self.printLPS(s, count, i+1, j-1)
            print(s[j], end='')
        elif count[i][j] == count[i+1][j]:
            self.printLPS(s, count, i+1, j)
        elif count[i][j] == count[i][j-1]:
            self.printLPS(s, count, i, j-1)


    '''
    Solution2的空间复杂度为O(n^2)
    进一步减少内存使用，我们发现计算第i行时只用到了第i+1行，这样我们便不需要n行，只需要2行即可

    起初先在第0行计算f[s.length()-1]，然后用第0行的结果在第1行计算f[s.length()-2]，再用第1行的结果在第0行计算f[s.length()-3]，以此类推。
    正在计算的那行设为now，那么计算第now行时，就要用第1-now行的结果。这种方法很巧妙。
    当计算完成时，如果s.length()是奇数，则结果在第0行；如果是偶数，则结果在第1行。
    此空间复杂度为O(n)
    '''
    def longestPalindrome3(self, s):
        count = [[0 for col in range(len(s))] for row in range(2)]
        now = 0
        for i in range(len(s) - 1, -1, -1):
            count[now][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    count[now][j] = count[1-now][j - 1] + 2
                else:
                    count[now][j] = max(count[now][j - 1], count[1-now][j])
            now = 1 - now
        if len(s) % 2 == 0:
            return count[1][len(s)-1]
        else:
            return count[0][len(s)-1]


solution = Solution()
print(solution.longestPalindrome1("abcfgbda", 0, len("abcfgbda") - 1))
print(solution.longestPalindrome2("abcfgbda"))
print(solution.longestPalindrome3("abcfgbda"))