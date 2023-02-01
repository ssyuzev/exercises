"""
A sawtooth sequence is a sequence of numbers that alternate between increasing and decreasing. In other words, each element is either strictly greater than its neighbouring elements or strictly less than its neighbouring elements.

PIC

Given an array of integers arr, your task is to count the number of contiguous subarrays that represent a sawtooth sequence of at least two elements.

Example

    For arr = [9, 8, 7, 6, 5], the output should be solution(arr) = 4.

    Since all the elements are arranged in decreasing order, it won't be possible to form any sawtooth subarrays of length 3 or more. There are 4 possible subarrays containing two elements, so the answer is 4.

    For arr = [10, 10, 10], the output should be solution(arr) = 0.

    Since all of the elements are equal, none of subarrays can be sawtooth, so the answer is 0.

    For arr = [1, 2, 1, 2, 1], the output should be solution(arr) = 10.

    All contiguous subarrays containing at least two elements satisfy the condition of problem. There are 10 possible contiguous subarrays containing at least two elements, so the answer is 10.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer arr

    An array of integers.

    Guaranteed constraints:
    2 ≤ arr.length ≤ 105,
    -109 ≤ arr[i] ≤ 109.

    [output] integer64

    Return the number of sawtooth subarrays.


Contiguous Subarray

An array made up of adjacent elements from another array.

For example, consider arr = [2, 3, 7]:

    [3, 7] is a contiguous subarray of arr
    [2, 3, 7] is a contiguous subarray of arr
    [7] is a contiguous subarray of arr
    [1, 2, 3] is not a contiguous subarray because it contains elements not in arr
    [2, 7] is not a contiguous subarray because the elements aren't adjacent in arr


"""
import timeit


from math import comb


def solution(arr):
    n=len(arr)
    if arr[1]!=arr[0]:
        l=2
        
    else:
        l=0
        
    pre = arr[1] - arr[0]
    ans=0
    
    for i in range(2,n):
        cur=arr[i] - arr[i-1]
        
        if cur*pre<0:
            l+=1
        else:
            if l==2:
                ans+=1
            elif l==0:
                ans+=0
            else:
                ans+=comb(l,2)
            if cur!=0:
                l=2
            else:
                l=0
        pre=cur
    if l==2:
        ans+=1
    elif l==0:
        ans+=0
    else:
        ans+=comb(l,2)
    return ans


if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5]  # result: 4
    start_time = timeit.default_timer()
    result = solution(arr)
    print(f"{result=}")
    print("*** The time difference is :", timeit.default_timer() - start_time)
    print("\n")
