# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):
    if not nums:
        return 0
    
    # Initialize max_product and min_product to the first element of the array
    max_product = min_product = result = nums[0]
    
    # Iterate over the rest of the array
    for num in nums[1:]:
        # Update max_product and min_product based on the current number
        candidates = [max_product * num, min_product * num, num]
        max_product = max(candidates)
        min_product = min(candidates)
        
        # Update result if the new max_product is greater than the current result
        result = max(result, max_product)
    
    return result
