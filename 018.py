"""
You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

NOTE: + refers to string concatenation.

Example

For s = "xzxzx", the output should be solution(s) = 5.

Consider all the ways to split s into three non-empty parts:

If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
Since there are five valid ways to split s, the answer is 5.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string to split.

Guaranteed constraints:
3 ≤ s.length ≤ 100.

[output] integer

The number of ways to split the given string.


"""
import timeit


def solution(s):
    n = len(s)
    count = 0 
    for i in range(1, n - 1): 
        for j in range(i + 1, n):
            s1 = s[0:i]
            s2 = s[i:j]
            s3 = s[j:n]
            if (s1 + s2 != s2 + s3) and (s2 + s3 != s3 + s1) and (s1 + s2 != s3 + s1): 
                count += 1
    return count


if __name__ == "__main__":
    s = "xzxzx"
    start_time = timeit.default_timer()
    result = solution(s)
    print(f"{result=}")
    print("*** The time difference is :", timeit.default_timer() - start_time)
