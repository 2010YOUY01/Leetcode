#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (36.41%)
# Total Accepted:    21.6K
# Total Submissions: 59.5K
# Testcase Example:  '"123456579"'
#
# Given a string S of digits, such as S = "123456579", we can split it into a
# Fibonacci-like sequence [123, 456, 579].
# 
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such
# that:
# 
# 
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
# type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# 
# 
# Also, note that when splitting the string into pieces, each piece must not
# have extra leading zeroes, except if the piece is the number 0 itself.
# 
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be
# done.
# 
# Example 1:
# 
# 
# Input: "123456579"
# Output: [123,456,579]
# 
# 
# Example 2:
# 
# 
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# 
# 
# Example 3:
# 
# 
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# 
# 
# Example 4:
# 
# 
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not
# valid.
# 
# 
# Example 5:
# 
# 
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# 
# 
# Note: 
# 
# 
# 1 <= S.length <= 200
# S contains only digits.
# 
# 
#
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def search(S: str, pre: int, cur: int, path: List[int]):
            # If found: save and return
            if not S:
                if pre != None and cur != None and len(path) >= 3:
                    yield path
                return
            # search forward
            # Only read 0 or 1 numbers
            elif pre == None:
                for i, _ in enumerate(S):
                    # Leading zeros are not allowed
                    if i > 0 and S[0] == '0': return
                    head = int(S[:i + 1])
                    yield from search(S[i + 1: ], cur, head, path + [head])
            # Have read >= 2 numbers
            else:
                expected = str(pre + cur)
                # F[i] <= 2**31 - 1
                if int(expected) > 2**31 - 1: return
                head = S[: len(expected)]
                if head == expected:
                    yield from search(S[len(expected): ], cur, pre + cur, path + [pre + cur])
        
        return next(search(S, None, None, []), [])
