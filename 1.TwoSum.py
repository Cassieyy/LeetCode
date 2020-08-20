'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)):
            if ((target-nums[i]) in nums[i+1:]):
                output.append(i)
                output.append(nums.index(target - nums[i], i+1))
                break

        return output


if __name__ == '__main__':
    nums = [1, 3, 4, 2]
    target = 6
    method = Solution()
    output = method.twoSum(nums, target)
    print(output)


        