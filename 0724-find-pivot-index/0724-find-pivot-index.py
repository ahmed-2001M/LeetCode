class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        freq = []
        freq.append(nums[0])
        for i in range(1,len(nums)):
            freq.append(nums[i]+freq[i-1]) 
        
        for i in range(len(nums)):
            if freq[-1] - freq[i] == freq[i] - nums[i]:
                return i
        return -1