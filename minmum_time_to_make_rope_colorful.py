# leetcode
#solutions of the leetcode problems
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        k=[]
        sum=0
        m=0
        for i in range(1,len(colors)):
            if colors[i-1]==colors[i]:
                m+=1
                if  neededTime[i-m]<=neededTime[i] and i-m not in k  :
                    k.append(i-m)
                else:
                    k.append(i)
            else:
                m=0
        for i in range(len(k)):
            sum+=neededTime[k[i]]
        return sum
