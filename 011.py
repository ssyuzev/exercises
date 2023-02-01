"""
You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".

PIC 011_1

You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective initial strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result. Note that occurrences in the initial strings are compared - they do not change over the merge process.

Given two strings s1 and s2, return the result of the special merge function you are implementing.

Example

For s1 = "dce" and s2 = "cccbd", the output should be
solution(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.

PIC 011_2

For s1 = "super" and s2 = "tower", the output should be
solution(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length ≤ 104.

[input] string s2

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length ≤ 104.

[output] string

The string that results by merging s1 and s2 using your special merge function.
"""
import timeit


from collections import Counter


def solution(s1, s2):
    s1_list, s2_list = [*s1], [*s2]
    s1_count = dict(Counter(s1))
    s2_count = dict(Counter(s2))
    result = ""
    while len(s1_list) or len(s2_list):
        try:
            if s1_count[s1_list[0]] < s2_count[s2_list[0]]:
                result += s1_list.pop(0)
            elif s1_count[s1_list[0]] == s2_count[s2_list[0]]:
                if s1_list[0] < s2_list[0]:
                    result += s1_list.pop(0)
                else:
                    result += s2_list.pop(0)
            else:
                result += s2_list.pop(0)
        except:
            if len(s2_list):
                result += "".join(s2_list)
                s2_list = []
            if len(s1_list):
                result += "".join(s1_list)
                s1_list = []
    return result


if __name__ == "__main__":
    expected = "owvieaqugtaleegvrabhugzyxgaegbxg"
    start_time = timeit.default_timer()
    result = solution(s1="ougtaleegvrabhugzyx", s2="owvieaqugaegbxggtaleegvrabhugzyx")
    if result != expected:
        print("!!! false")
    print(f"{result=} \n{expected=}")  # Expected Output: "owvieaqugtaleegvrabhugzyxgaegbxg"
    print("*** The time difference is :", timeit.default_timer() - start_time)
