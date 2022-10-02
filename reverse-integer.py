class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m=1
        if(x<0):
            m=0
        if(x>2147483647)or(x<-2147483648):
            return 0
        x=abs(x)
        a=0
        l=len(str(x))
        k=10**(l-1)

        while(x>0):
            n=x%10
            a+=k*n
            k/=10
            x/=10
        if(a>2147483647)or(a<-2147483648):
            return 0
        if m==0:
            a=-a
        return abs