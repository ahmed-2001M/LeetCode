class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) : return -1

        start = 0
        sm = 0
        for idx , val in enumerate(gas):
            sm += (gas[idx] - cost[idx])
            if sm < 0:
                sm = 0 
                start = idx+1
        return start