class Solution:
    '''
    Algorithm:
    calculate the current capacity 
        if it is > 0 then we continue to the next and add the next's capacity 
        if it is < 0 then we change the start and keep track of the deficit
        we keep doing this unil we reach the end of the gas station 
    after this we iterate from the beginning to the start and calculate the capacity by involving the deficit. At the end of this iteration if the capacity is >=0 then it's a valid tour, else it is not.
    Time Complexity = O(N)
    Space Complexity = O(1)
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        capacity = 0 
        deficit = 0
        start = 0 
        for i in range(len(gas)):
            capacity += gas[i] - cost[i]
            
            if capacity < 0:
                start = i+1
                deficit += capacity
                capacity = 0 
        
        for i in range(start):
            capacity += gas[i] - cost[i]
            if capacity < 0:
                return -1
        return start
