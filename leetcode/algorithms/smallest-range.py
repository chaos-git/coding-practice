'''
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.
'''


from Queue import PriorityQueue

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pointers = [len(numbers) - 1 for numbers in nums]
        get_val = lambda i: nums[i][pointers[i]]

        min_delta = None
        min_range = None
        while True:
            min_index = None
            max_index = None
            for numbers_index, numbers in enumerate(nums):
                if min_index is None or get_val(numbers_index) < get_val(min_index):
                    min_index = numbers_index
                if max_index is None or get_val(numbers_index) > get_val(max_index):
                    max_index = numbers_index
            min_value = get_val(min_index)
            max_value = get_val(max_index)
            if min_delta is None or min_delta >= max_value - min_value:
                min_delta = max_value - min_value
                min_range = (min_value, max_value)
            pointers[max_index] -= 1
            if pointers[max_index] < 0:
                break

        return min_range
