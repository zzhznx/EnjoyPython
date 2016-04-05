class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = []
        for i in range(n):
            l = [0 for j in range(n)]
            matrix.append(l)

        up = 0
        left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1

        direct = 0

        count = 1

        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    matrix[up][i] = count
                    count += 1
                up += 1
            if direct == 1:
                for i in range(up, down + 1):
                    matrix[i][right] = count
                    count += 1
                right -= 1
            if direct == 2:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = count
                    count += 1
                down -= 1
            if direct == 3:
                for i in range(down, up -1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1
            if up > down or left > right:
                return matrix
            direct = (direct + 1) % 4

print(Solution().generateMatrix(3))