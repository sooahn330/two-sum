def twoSum(nums:List[int],target : int) -> List[int]:
    for first in range(len[nums]):
        for second in range(first+1,len[nums]):
            if nums[first] + nums[second] == target:
                return [first,second]
