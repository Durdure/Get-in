class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}
        
        for i, x in enumerate(nums):
            if x not in left:
                left[x]=i
            right[x] = i
            count[x] =count.get(x,0)+1
        answer =len(nums)
        degree= max(count.values())
        
        for x in count:
            if count[x] == degree:
                answer = min(answer, right[x]-left[x]+1)
        return answer