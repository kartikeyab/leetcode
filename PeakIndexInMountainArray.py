class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        largestNum = float("-inf")
        for num in A:
            if num > largestNum:
                largestNum = num
        return A.index(largestNum)

#usign Binary Search
    class Solution(object):

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = 0
        R = len(A)-1
        
        while L<=R:
            mid = (L+R)//2
            if A[mid-1]<A[mid]>A[mid+1]:
                return mid
            elif A[mid-1]<A[mid]<A[mid+1]:
                L = mid+1
            elif A[mid-1]>A[mid]>A[mid+1]:
                R = mid-1
