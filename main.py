class Solution(object):

    def find_num(self, num, target):
        num_to_find = target - num
        return num_to_find

    def twoSum(self, nums, target):
        num_dict = {}
        two_sum_indexes = []
        for idx, num in enumerate(nums):
            # num_dict[num] = idx
            num_to_find = self.find_num(num, target)
            print(num_dict)
            if num_to_find in num_dict:
                two_sum_indexes = [num_dict[num_to_find], idx]
                # return two_sum_indexes
            else:
                num_dict[num] = idx

        if len(two_sum_indexes) > 0:
            print(two_sum_indexes)
        else:
            print("We could not find any two such numbers")



num_array = [3,3]
target = 6
solution = Solution()
solution.twoSum(num_array, target)

