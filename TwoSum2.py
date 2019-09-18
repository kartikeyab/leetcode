class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in numbers:
            j = target - i
            if j not in dic:
                dic[i] = True
            else:
                arr =[numbers.index(j)+1,numbers.index(i)+1]
                if arr[0]==arr[1]:
                    arr[1]+=1
                return arr
            
