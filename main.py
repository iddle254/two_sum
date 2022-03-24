class Solution(object):

 class Solution(object):
    def find_num(self, num, target):
        num_to_find = target - num
        return num_to_find
    
    def find_two_sum(self, num_dict, num_to_find, idx):
        two_sum_indexes = [num_dict[num_to_find], idx]
        return two_sum_indexes

    def twoSum(self, nums, target):
        num_dict = {}
        two_sum_indexes = []
        for idx, num in enumerate(nums):
            num_to_find = self.find_num(num, target)
            if num_to_find in num_dict:
                two_sum_indexes = self.find_two_sum(num_dict, num_to_find, idx)
                return two_sum_indexes
            else:
                num_dict[num] = idx



num_array = [3,3]
target = 6
solution = Solution()
solution.twoSum(num_array, target)

