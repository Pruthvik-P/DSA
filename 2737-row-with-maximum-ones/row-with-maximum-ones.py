class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxOnesInx, maxOnesCount = 0, 0
        for i, row in enumerate(mat):
            ones = sum(row)

            if ones > maxOnesCount :
                maxOnesInx, maxOnesCount = i, ones

        return [maxOnesInx, maxOnesCount]
        