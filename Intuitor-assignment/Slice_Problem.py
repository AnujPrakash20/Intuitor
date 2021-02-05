"""
You are given an array A consisting of the integers −1, 0 and 1. A slice of that array is
any pair of integers (P, Q) such that 0 ≤ P ≤ Q < N. Your task is to find the longest slice
of A whose elements yield a non-negative sum.
Write a function:
def solution(A)
that, given an array A of length N, consisting only of the values −1, 0, 1, returns the
length of the longest slice of A that yields a non-negative sum. If there's no such slice,
your function should return 0.
For example, given A = [−1, −1, 1, −1, 1, 0, 1, −1, −1], your function should return 7, as
the slice starting at the second position and ending at the eighth is the longest slice with
a non-negative sum.
For another example, given A = [1, 1, −1, −1, −1, −1, −1, 1, 1] your function should
return 4: both the first four elements and the last four elements of array A are longest
valid slices.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1..1].
"""


class Slice():
    def dp1(self,arr):
        dp = [arr[0]]

        n = len(arr)
        for i in range(1,n):

            dp.append(dp[-1]+arr[i])

        return dp


    def solution(self,arr):
        d = {}
        for i,v in enumerate(arr):
            d[v]=i

        max_len = 0
        for i,v in enumerate(arr):
            max_len = max(max_len,d[v]-i) #Negative numbers are ignored from the front to make it zero.
        return max_len

if __name__ == "__main__":
    s=Slice()
    A = list(map(int,input().split()))
    print(s.solution(s.dp1(A)))
    #out - 7
