class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tup = set()

        for i in nums:
            if i in tup:
                return True
            tup.add(i)
        return False

