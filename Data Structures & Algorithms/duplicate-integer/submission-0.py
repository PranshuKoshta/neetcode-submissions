class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for x in nums:
            if x in store:
                return True
            store.add(x)
        
        return False
