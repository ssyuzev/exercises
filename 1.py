def solution(a):
    b = list()
    for index, item in enumerate(a):
        if index == 0:
            prev_element = 0
        else:
            try:
                prev_element = a[index - 1]
            except Exception:
                prev_element = 0
        try:
            next_element = a[index + 1]
        except Exception:
            next_element = 0
        element = prev_element + item + next_element
        b.append(element)
    return b


if __name__ == "__main__":
    print(solution([4, 0, 1, -2, 3]))


"""

Given an array a, your task is to apply the following mutation to it:

Array a mutates into a new array b of the same length
For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
For example, b[0] equals 0 + a[0] + a[1]
Example

For a = [4, 0, 1, -2, 3], the output should be solution(a) = [4, 5, -1, 2, 1].

Explanation:

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the mutated answer array is [4, 5, -1, 2, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of integers that needs to be mutated.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-103 ≤ a[i] ≤ 103.

[output] array.integer

The resulting array after the mutation.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""
