from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums:
            max_product, cur_product_max, cur_product_min = nums[0], nums[0], nums[0]
            for i in range(1, len(nums)):
                cur_product_max, cur_product_min = max(nums[i], cur_product_min*nums[i], cur_product_max*nums[i]), min(nums[i], cur_product_min*nums[i], cur_product_max*nums[i])
                max_product = max(cur_product_max, max_product)
            return max_product
        else:
            return 0
A = Solution()
a = [6,-1,-7,2]
print(A.maxProduct(a))

  

