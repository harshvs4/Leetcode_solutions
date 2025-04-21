class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        maxPref, minPref, curr = 0, 0, 0

        for d in differences:
            curr += d
            minPref = min(minPref, curr)
            maxPref = max(maxPref, curr)

        return max(0, (upper-maxPref) - (lower-minPref)+1)