def single_number(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = result ^ nums[i] 

single_number([2,2,1])