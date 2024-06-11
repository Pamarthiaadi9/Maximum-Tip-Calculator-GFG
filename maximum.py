from typing import List


class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        v = []
        for i in range(len(arr)):
            v.append((abs(arr[i] - brr[i]), (arr[i], brr[i])))
        v.sort(reverse=True)

        ans = 0
        for i in range(len(v)):
            if x == 0:
                ans += v[i][1][1]
            elif y == 0:
                ans += v[i][1][0]
            else:
                if v[i][1][0] > v[i][1][1]:
                    x -= 1
                    ans += v[i][1][0]
                else:
                    y -= 1
                    ans += v[i][1][1]
        return ans
